import http.server
import socketserver
import os
import sys
import json
import urllib.parse
import webbrowser

DIR_RAIZ = os.path.dirname(os.path.abspath(__file__))
DIR_FRONTEND = os.path.join(DIR_RAIZ, "frontend")
DIR_DATOS = os.path.join(DIR_RAIZ, "datos")
RUTA_CSV_BASE = os.path.join(DIR_DATOS, "paises.csv")
RUTA_CSV_COMPLETO = os.path.join(DIR_DATOS, "paises_mundo_completo.csv")

sys.path.insert(0, DIR_RAIZ)

from modulos.archivos import cargar_paises_csv, guardar_paises_csv
from modulos.validaciones import (
    validar_datos_nuevo_pais,
    validar_datos_actualizacion_pais,
    validar_filtros_query,
)
from modulos.operaciones import (
    agregar_pais,
    actualizar_pais,
    buscar_pais_por_nombre,
    filtrar_por_continente,
    filtrar_por_rango_poblacion,
    filtrar_por_rango_superficie,
)
from modulos.ordenamiento import ordenar_paises
from modulos.estadisticas import generar_resumen_estadistico

# Configuración de puerto dinámica (para despliegue en Render, Railway, Fly, etc.)
PUERTO = int(os.environ.get("PORT", 8000))

# Carga inicial de datos en memoria
archivo_inicial = RUTA_CSV_COMPLETO if os.path.exists(RUTA_CSV_COMPLETO) else RUTA_CSV_BASE
paises_memoria = cargar_paises_csv(archivo_inicial)


class GestorHTTPPaises(http.server.SimpleHTTPRequestHandler):
    """
    Servidor web HTTP que combina:
    - API REST con validaciones completas del lado del backend.
    - Servicio de archivos estáticos (Frontend SPA HTML/CSS/JS).
    - Soporte CORS y respuestas JSON estructuradas.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR_FRONTEND, **kwargs)

    def responder_json(self, datos, codigo=200):
        cuerpo = json.dumps(datos, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(cuerpo)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    # ==========================================================================
    # PETICIONES GET
    # ==========================================================================
    def do_GET(self):
        global paises_memoria
        parsed_url = urllib.parse.urlparse(self.path)
        ruta = parsed_url.path
        query = urllib.parse.parse_qs(parsed_url.query)

        # Endpoint: Listado de países con validación de filtros y ordenamiento en el Backend
        if ruta == "/api/paises":
            # 1. Validación en el backend de los parámetros de consulta
            valido, filtros, errores = validar_filtros_query(query)
            if not valido:
                self.responder_json({
                    "exito": False,
                    "mensaje": "Parámetros de consulta inválidos.",
                    "errores": errores
                }, 400)
                return

            resultado = list(paises_memoria)

            # 2. Aplicación de búsqueda
            if filtros["busqueda"]:
                resultado = buscar_pais_por_nombre(
                    resultado,
                    filtros["busqueda"],
                    coincidencia_exacta=filtros["exacta"]
                )

            # 3. Filtro por continente
            if filtros["continente"] != "todos":
                resultado = filtrar_por_continente(resultado, filtros["continente"])

            # 4. Filtro por rango de población
            if filtros["min_pob"] is not None and filtros["max_pob"] is not None:
                resultado = filtrar_por_rango_poblacion(resultado, filtros["min_pob"], filtros["max_pob"])

            # 5. Filtro por rango de superficie
            if filtros["min_sup"] is not None and filtros["max_sup"] is not None:
                resultado = filtrar_por_rango_superficie(resultado, filtros["min_sup"], filtros["max_sup"])

            # 6. Ordenamiento en el Backend (Bubble Sort con soporte ascendente / descendente)
            resultado = ordenar_paises(
                resultado,
                clave=filtros["orden_clave"],
                descendente=filtros["orden_desc"]
            )

            self.responder_json({
                "exito": True,
                "total": len(resultado),
                "total_global": len(paises_memoria),
                "filtros_aplicados": filtros,
                "paises": resultado
            })
            return

        # Endpoint: Métricas estadísticas calculadas en el Backend
        elif ruta == "/api/estadisticas":
            resumen = generar_resumen_estadistico(paises_memoria)
            self.responder_json({
                "exito": True,
                "estadisticas": resumen
            })
            return

        # Endpoints para descarga de archivos CSV de datos
        elif ruta == "/datos/paises.csv":
            self.servir_archivo_externo(RUTA_CSV_BASE, "text/csv; charset=utf-8")
            return
        elif ruta == "/datos/paises_mundo_completo.csv":
            self.servir_archivo_externo(RUTA_CSV_COMPLETO, "text/csv; charset=utf-8")
            return

        # Archivos estáticos del frontend (HTML, CSS, JS)
        return super().do_GET()

    # ==========================================================================
    # PETICIONES POST
    # ==========================================================================
    def do_POST(self):
        global paises_memoria
        parsed_url = urllib.parse.urlparse(self.path)
        ruta = parsed_url.path

        # Endpoint: Alta de nuevo país con validaciones estrictas de backend
        if ruta == "/api/paises":
            longitud = int(self.headers.get("Content-Length", 0))
            if longitud == 0:
                self.responder_json({
                    "exito": False,
                    "mensaje": "El cuerpo de la solicitud no puede estar vacío.",
                    "errores": ["No se enviaron datos."]
                }, 400)
                return

            cuerpo = self.rfile.read(longitud)
            try:
                datos = json.loads(cuerpo.decode("utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError):
                self.responder_json({
                    "exito": False,
                    "mensaje": "Formato JSON inválido en la solicitud.",
                    "errores": ["El cuerpo enviado no es un JSON válido."]
                }, 400)
                return

            # Ejecutar validaciones del Backend
            valido, datos_limpios, errores = validar_datos_nuevo_pais(datos, paises_memoria)
            if not valido:
                self.responder_json({
                    "exito": False,
                    "mensaje": "Error de validación en los datos del país.",
                    "errores": errores
                }, 400)
                return

            # Agregar país validado
            exito = agregar_pais(
                paises_memoria,
                datos_limpios["nombre"],
                datos_limpios["poblacion"],
                datos_limpios["superficie"],
                datos_limpios["continente"]
            )

            if exito:
                # Persistencia en CSV
                archivo_guardado = RUTA_CSV_COMPLETO if os.path.exists(RUTA_CSV_COMPLETO) else RUTA_CSV_BASE
                guardar_paises_csv(archivo_guardado, paises_memoria)
                self.responder_json({
                    "exito": True,
                    "mensaje": f"País '{datos_limpios['nombre']}' registrado exitosamente.",
                    "pais": datos_limpios
                }, 201)
            else:
                self.responder_json({
                    "exito": False,
                    "mensaje": "No se pudo registrar el país en el sistema.",
                    "errores": ["Error interno al registrar el país."]
                }, 500)
            return

        # Endpoint: Recargar dataset base (25 países)
        elif ruta == "/api/recargar-base":
            paises_memoria = cargar_paises_csv(RUTA_CSV_BASE)
            self.responder_json({
                "exito": True,
                "mensaje": "Dataset base recargado.",
                "total": len(paises_memoria)
            })
            return

        # Endpoint: Recargar dataset mundial completo (60 países)
        elif ruta == "/api/recargar-completo":
            paises_memoria = cargar_paises_csv(RUTA_CSV_COMPLETO)
            self.responder_json({
                "exito": True,
                "mensaje": "Dataset mundial ampliado recargado.",
                "total": len(paises_memoria)
            })
            return

        self.responder_json({"exito": False, "mensaje": "Ruta no encontrada."}, 404)

    # ==========================================================================
    # PETICIONES PUT
    # ==========================================================================
    def do_PUT(self):
        global paises_memoria
        parsed_url = urllib.parse.urlparse(self.path)
        ruta = parsed_url.path

        # Endpoint: Actualización de datos de un país existente
        if ruta == "/api/paises":
            longitud = int(self.headers.get("Content-Length", 0))
            if longitud == 0:
                self.responder_json({
                    "exito": False,
                    "mensaje": "El cuerpo de la solicitud no puede estar vacío.",
                    "errores": ["No se enviaron datos."]
                }, 400)
                return

            cuerpo = self.rfile.read(longitud)
            try:
                datos = json.loads(cuerpo.decode("utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError):
                self.responder_json({
                    "exito": False,
                    "mensaje": "Formato JSON inválido en la solicitud.",
                    "errores": ["El cuerpo enviado no es un JSON válido."]
                }, 400)
                return

            # Ejecutar validaciones del Backend
            valido, datos_limpios, errores = validar_datos_actualizacion_pais(datos, paises_memoria)
            if not valido:
                self.responder_json({
                    "exito": False,
                    "mensaje": "Error de validación al actualizar datos.",
                    "errores": errores
                }, 400)
                return

            exito = actualizar_pais(
                paises_memoria,
                datos_limpios["nombre"],
                datos_limpios["poblacion"],
                datos_limpios["superficie"]
            )

            if exito:
                archivo_guardado = RUTA_CSV_COMPLETO if os.path.exists(RUTA_CSV_COMPLETO) else RUTA_CSV_BASE
                guardar_paises_csv(archivo_guardado, paises_memoria)
                self.responder_json({
                    "exito": True,
                    "mensaje": f"Datos del país '{datos_limpios['nombre']}' actualizados correctamente.",
                    "pais": datos_limpios
                }, 200)
            else:
                self.responder_json({
                    "exito": False,
                    "mensaje": "No se pudo actualizar el país en el dataset.",
                    "errores": ["El país especificado no fue encontrado."]
                }, 404)
            return

        self.responder_json({"exito": False, "mensaje": "Ruta no encontrada."}, 404)

    def servir_archivo_externo(self, ruta_completa, content_type):
        if not os.path.exists(ruta_completa):
            self.send_error(404, "Archivo no encontrado")
            return

        with open(ruta_completa, "rb") as f:
            contenido = f.read()

        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(contenido)))
        self.end_headers()
        self.wfile.write(contenido)


# ==============================================================================
# Arranque del servidor
# ==============================================================================
def iniciar_servidor():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PUERTO), GestorHTTPPaises) as httpd:
        host = "localhost" if "PORT" not in os.environ else "0.0.0.0"
        url = f"http://{host}:{PUERTO}"
        print("=" * 70)
        print("   SERVIDOR WEB - GESTIÓN DE PAÍSES (TPI PROGRAMACIÓN 1 - UTN)")
        print("=" * 70)
        print(f" • Servidor activo en: {url}")
        print(f" • Puerto:             {PUERTO}")
        print(f" • Carpeta frontend:   {DIR_FRONTEND}")
        print(f" • Países cargados:    {len(paises_memoria)}")
        print(" • Presione CTRL + C en esta consola para detener el servidor.")
        print("=" * 70)

        # Abrir navegador automáticamente solo en entornos locales de desarrollo
        if "PORT" not in os.environ and "RENDER" not in os.environ and "DYNO" not in os.environ:
            try:
                webbrowser.open(url)
            except Exception:
                pass

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor web detenido por el usuario.")


if __name__ == "__main__":
    iniciar_servidor()
