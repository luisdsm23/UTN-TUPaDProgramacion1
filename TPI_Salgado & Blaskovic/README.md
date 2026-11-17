# Sistema de Gestión de Datos de Países en Python

**Trabajo Práctico Integrador (TPI) - Programación 1**  
**Tecnicatura Universitaria en Programación a Distancia**  
**Universidad Tecnológica Nacional (UTN)**

---

## 📌 Enlaces Obligatorios de Entrega

- 🎥 **Video Demostrativo (YouTube / Drive con acceso público):** `[INSERTAR_AQUI_LINK_DEL_VIDEO]`  
  *(Duración: 10 a 15 minutos explicando estructura de datos y todos los flujos de consola)*
- 📄 **Documentación Académica y Técnica en PDF:** [Documentacion_TPI.pdf](Documentacion_TPI.pdf) *(Disponible en la raíz de este proyecto o en: `[INSERTAR_AQUI_LINK_DEL_PDF_SI_SE_ALOJA_EXTERNAMENTE]`)*
- 💻 **Repositorio en GitHub:** [https://github.com/luisdsm23/UTN-TUPaDProgramacion1](https://github.com/luisdsm23/UTN-TUPaDProgramacion1)

---

## 👥 Integrantes del Equipo y Participación

- **Comisión:** Comisión 2 - Turno Tarde (ambos integrantes)

| Nombre y Apellido | Legajo / DNI | Correo Electrónico | Porcentaje de Participación |
| :--- | :--- | :--- | :---: |
| **Luis Salgado** | 55266 | luis.salgado@alumnos.frm.utn.edu.ar | 50% |
| **Branko Blaskovic** | 55302 | branko.blaskovic@alumnos.frm.utn.edu.ar | 50% |

> **División de Tareas:**
> - **Luis Salgado:** Diseño de estructuras de datos (listas de diccionarios), desarrollo de módulos de archivos CSV (`archivos.py`), validaciones de entrada (`validaciones.py`), y redacción del marco teórico del informe.
> - **Branko Blaskovic:** Implementación de lógica de operaciones (`operaciones.py`), algoritmos de ordenamiento clásico (`ordenamiento.py`), cálculo de métricas estadísticas (`estadisticas.py`), interfaz de consola (`main.py` y `interfaz.py`) y diagramas de flujo.

---

## 📖 Descripción del Programa

Esta aplicación de consola desarrollada en **Python 3.x** permite gestionar un dataset de países a nivel global. El sistema aplica buenas prácticas de programación estructurada, modularización (respetando el principio de una función = una responsabilidad), algoritmos de ordenamiento, manipulación de listas y diccionarios, y persistencia en archivos CSV.

### Dominio de Datos
Cada país está modelado mediante un diccionario con los siguientes atributos:
- `nombre` *(str)*: Nombre oficial o común del país (único).
- `poblacion` *(int)*: Cantidad total de habitantes (entero positivo).
- `superficie` *(int)*: Área territorial en kilómetros cuadrados (km², entero positivo).
- `continente` *(str)*: Continente al que pertenece geográficamente.

---

## 🚀 Funcionalidades Principales

1. **Listado General:** Visualización tabular con columnas formateadas y números con separadores de miles.
2. **Alta de País:** Inserción de un nuevo país validando que no existan campos vacíos, valores numéricos inválidos ni países duplicados.
3. **Actualización de Datos:** Modificación controlada de la población y superficie de un país existente.
4. **Búsqueda Flexible:** Búsqueda por nombre mediante **coincidencia exacta** o **coincidencia parcial** (insensible a mayúsculas y acentos diacríticos).
5. **Filtrado Avanzado:**
   - Por continente.
   - Por rango numérico de población (mínimo y máximo con validación en backend).
   - Por rango numérico de superficie / territorio en km² (mínimo y máximo con validación en backend).
6. **Ordenamiento Algorítmico Parametrizable (Ascendente y Descendente):**
   - **Por Nombre de País:** Orden alfabético Ascendente (A-Z) o Descendente (Z-A), insensible a tildes y mayúsculas.
   - **Por Población:** Ascendente (de menor a mayor población) o Descendente (de mayor a menor).
   - **Por Superficie / Territorio:** Ascendente (de menor a mayor extensión territorial) o Descendente (de mayor a menor).
   - **Por Continente:** Agrupación alfabética ascendente o descendente.
   - Implementado mediante **Bubble Sort (Ordenamiento Burbuja)** nativo con bandera de parada temprana (`hubo_intercambio`).
   - Disponible tanto en la consola como de forma reactiva e interactiva en la interfaz web (vía selectores y clics en cabeceras de tabla).
7. **Validaciones Robustas del Backend (API y Consola):**
   - Validación tipada y de reglas de negocio en Python para altas, modificaciones, búsquedas y rangos.
   - Rechazo de valores vacíos, tipos erróneos, rangos cruzados (`min > max`) y países duplicados con respuestas HTTP 400 detalladas.
8. **Estadísticas Clave:**
   - País con mayor y menor población.
   - Promedio general de población.
   - Promedio general de superficie.
   - Frecuencia y distribución porcentual de países por continente con barra visual.
8. **Persistencia e Integridad:**
   - Lectura y escritura en `datos/paises.csv`.
   - Control de excepciones ante archivos corruptos, faltantes o con columnas incorrectas.
   - Advertencia de cambios sin guardar antes de salir del sistema.

---

## 📁 Estructura del Proyecto

```text
TPI_Paises/
├── datos/
│   ├── paises.csv                     # Dataset base (25 países para la consola y pruebas)
│   └── paises_mundo_completo.csv      # Dataset mundial ampliado (60 países de todos los continentes)
├── modulos/
│   ├── __init__.py                    # Inicializador de paquete Python
│   ├── archivos.py                    # Lectura y guardado de CSV con manejo de errores
│   ├── operaciones.py                 # Altas, actualizaciones, búsquedas y filtros
│   ├── ordenamiento.py                # Algoritmo de ordenamiento burbuja parametrizable
│   ├── estadisticas.py                # Métricas, promedios, extremos y frecuencias
│   ├── validaciones.py                # Validación de enteros, cadenas no vacías y rangos
│   └── interfaz.py                    # Formateo de tablas y menús estilizados en consola
├── frontend/                          # Interfaz Web Interactiva (SPA moderna)
│   ├── index.html                     # Tablas ordenables accesibles, modales <dialog> y KPIs
│   ├── styles.css                     # Diseño responsivo con soporte de Modo Oscuro/Claro
│   └── app.js                         # Ordenamiento Intl.Collator, filtros en vivo y carga CSV
├── app_web.py                         # Servidor web local en Python nativo (sin dependencias)
├── main.py                            # Punto de entrada y menú interactivo en consola
├── test_tpi.py                        # Suite de 10 pruebas unitarias con unittest (10/10 OK)
├── generar_pdf.py                     # Script para compilar el informe académico oficial
├── Documentacion_TPI.md               # Informe académico completo en formato Markdown
├── Documentacion_TPI.pdf              # Documento PDF oficial de entrega
└── README.md                          # Este archivo descriptivo
```

---

## 🛠️ Instalación y Requisitos

- **Python 3.10 o superior** (compatible con Python 3.14).
- **Sin dependencias obligatorias**: Tanto el sistema de consola como el servidor web corren sobre la biblioteca estándar de Python sin necesidad de instalar frameworks externos.
- **ReportLab** (opcional, solo si se desea recompilar el PDF):
  ```bash
  pip install reportlab
  ```

---

## 💻 Instrucciones de Uso

### 1. Iniciar la Interfaz Web Interactiva (Frontend)
```bash
python app_web.py
```
> Esto iniciará el servidor local en `http://localhost:8000` y abrirá automáticamente tu navegador web con la interfaz gráfica interactiva.  
> *Alternativamente, también puedes abrir directamente el archivo `frontend/index.html` en cualquier navegador web sin necesidad de ejecutar ningún comando.*

### 2. Ejecutar la Aplicación en Consola (CLI Tradicional)
```bash
python main.py
```

### 3. Ejecutar los tests unitarios
```bash
python -m unittest test_tpi.py
```

### 4. Regenerar la documentación académica en PDF
```bash
python generar_pdf.py
```

---

## 🌐 Guía de Despliegue en la Nube (Compartir Link al Profesor)

Para que el docente pueda probar la aplicación directamente sin instalar nada en su computadora, dispones de dos alternativas recomendadas y gratuitas:

### Opción 1: Despliegue en Render.com (Recomendada - Backend Python en Vivo)
El proyecto ya cuenta con `render.yaml`, `Procfile` y detección automática de variables de entorno para correr sin fricciones:
1. Sube tu proyecto a un repositorio en **GitHub**.
2. Entra en [Render.com](https://render.com/) e inicia sesión con tu cuenta de GitHub (100% gratuito, sin tarjeta de crédito).
3. Haz clic en **New +** y selecciona **Web Service**.
4. Conecta el repositorio de tu TPI.
5. Configura los campos básicos:
   - **Name:** `tpi-paises-utn` (o el nombre que elijas).
   - **Environment:** `Python 3`.
   - **Build Command:** `pip install -r requirements.txt`.
   - **Start Command:** `python app_web.py`.
6. Haz clic en **Deploy Web Service**.
7. En 2 minutos tendrás una URL pública HTTPS (ej. `https://tpi-paises-utn.onrender.com`) lista para compartir en la entrega del campus virtual.

### Opción 2: Despliegue en GitHub Pages (Frontend SPA Inmediato)
Como la carpeta `frontend/` es una aplicación web autónoma que incluye el dataset de respaldo:
1. En tu repositorio de GitHub, ve a **Settings** > **Pages**.
2. En **Source**, selecciona la rama `main` y la carpeta correspondiente (`/` o `/docs` moviendo los archivos de `frontend`).
3. Obtendrás un enlace instantáneo tipo `https://tu-usuario.github.io/tu-repositorio/frontend/`.

---

## 🖥️ Ejemplos de Entradas y Salidas

### Ejemplo 1: Menú Principal y Listado de Países
```text
================================================================================
            TRABAJO PRÁCTICO INTEGRADOR: GESTIÓN DE DATOS DE PAÍSES             
                    Tecnicatura Universitaria en Programación - UTN             
================================================================================
[ÉXITO] Se cargaron 25 países correctamente desde 'datos/paises.csv'.

==================================================
                 MENÚ PRINCIPAL
==================================================
 1. Listar todos los países
 2. Agregar un nuevo país
 3. Actualizar datos de un país (Población y Superficie)
 4. Buscar país por nombre (parcial o exacta)
 5. Filtrar países (por continente, población o superficie)
 6. Ordenar países (por nombre, población o superficie)
 7. Mostrar estadísticas
 8. Guardar cambios en el archivo CSV
 9. Recargar dataset desde CSV
 0. Salir
==================================================
Seleccione una opción: 1

+------+--------------------------+----------------+--------------------+--------------------+
|  Nº  | País                     | Continente     |    Población (hab) |   Superficie (km²) |
+------+--------------------------+----------------+--------------------+--------------------+
|    1 | Argentina                | América        |         45.376.763 |          2.780.400 |
|    2 | Japón                    | Asia           |        125.800.000 |            377.975 |
|    3 | Brasil                   | América        |        213.993.437 |          8.515.767 |
|    4 | Alemania                 | Europa         |         83.149.300 |            357.022 |
+------+--------------------------+----------------+--------------------+--------------------+
```

### Ejemplo 2: Búsqueda de un país por coincidencia parcial
```text
Seleccione una opción: 4
Tipo de búsqueda:
1. Coincidencia Parcial
2. Coincidencia Exacta
Seleccione el tipo de búsqueda (1/2): 1
Ingrese el término de búsqueda: jap

+------+--------------------------+----------------+--------------------+--------------------+
|  Nº  | País                     | Continente     |    Población (hab) |   Superficie (km²) |
+------+--------------------------+----------------+--------------------+--------------------+
|    1 | Japón                    | Asia           |        125.800.000 |            377.975 |
+------+--------------------------+----------------+--------------------+--------------------+
```

### Ejemplo 3: Cálculo y Presentación de Estadísticas
```text
Seleccione una opción: 7

================================================================================
                       ESTADÍSTICAS GENERALES DEL SISTEMA                       
================================================================================
 • Total de países analizados: 25
--------------------------------------------------------------------------------
 • País con MAYOR población: China (Asia) con 1.412.000.000 habitantes.
 • País con MENOR población: Uruguay (América) con 3.485.152 habitantes.
--------------------------------------------------------------------------------
 • Promedio de población:  185.187.351,04 habitantes por país.
 • Promedio de superficie: 2.378.117,16 km² por país.
--------------------------------------------------------------------------------
 • Distribución de países por continente:
   - América        :   6 país(es) ( 24.0%)  ████
   - Asia           :   4 país(es) ( 16.0%)  ███
   - Europa         :   7 país(es) ( 28.0%)  █████
   - Oceanía        :   2 país(es) (  8.0%)  █
   - África         :   6 país(es) ( 24.0%)  ████
================================================================================
```

---

## ⚖️ Licencia y Uso Académico
Proyecto desarrollado para fines pedagógicos exclusivos en la cátedra de Programación 1 de la Universidad Tecnológica Nacional.
