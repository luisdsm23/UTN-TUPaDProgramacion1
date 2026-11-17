import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modulos.archivos import cargar_paises_csv, guardar_paises_csv
from modulos.validaciones import (
    validar_texto_no_vacio,
    validar_entero_positivo,
    validar_rango_enteros,
    validar_opcion_menu,
)
from modulos.operaciones import (
    agregar_pais,
    actualizar_pais,
    buscar_pais_por_nombre,
    filtrar_por_continente,
    filtrar_por_rango_poblacion,
    filtrar_por_rango_superficie,
    obtener_continentes_unicos,
)
from modulos.ordenamiento import ordenar_paises
from modulos.estadisticas import generar_resumen_estadistico
from modulos.interfaz import (
    mostrar_titulo,
    mostrar_tabla_paises,
    mostrar_estadisticas_en_consola,
    pausar_consola,
)

RUTA_CSV_DEFAULT = os.path.join(os.path.dirname(__file__), "datos", "paises.csv")


# Alta de pais
def menu_agregar_pais(paises: list[dict]) -> bool:
    mostrar_titulo("AGREGAR NUEVO PAÍS")
    nombre = validar_texto_no_vacio("Ingrese el nombre del país: ", "Nombre")
    poblacion = validar_entero_positivo("Ingrese la población (habitantes): ", "Población")
    superficie = validar_entero_positivo("Ingrese la superficie (km²): ", "Superficie")
    
    continentes_existentes = obtener_continentes_unicos(paises)
    if continentes_existentes:
        print(f"Continentes ya registrados: {', '.join(continentes_existentes)}")
    continente = validar_texto_no_vacio("Ingrese el continente: ", "Continente")

    return agregar_pais(paises, nombre, poblacion, superficie, continente)


# Modificacion de pais
def menu_actualizar_pais(paises: list[dict]) -> bool:
    mostrar_titulo("ACTUALIZAR DATOS DE UN PAÍS")
    if not paises:
        print("[ERROR] No hay países cargados en el sistema.")
        return False

    nombre = validar_texto_no_vacio("Ingrese el nombre del país que desea actualizar: ", "Nombre")
    coincidencias = buscar_pais_por_nombre(paises, nombre, coincidencia_exacta=True)
    
    if not coincidencias:
        sugerencias = buscar_pais_por_nombre(paises, nombre, coincidencia_exacta=False)
        if sugerencias:
            print(f"[INFO] No se encontró coincidencia exacta para '{nombre}', pero se hallaron sugerencias:")
            for s in sugerencias:
                print(f"  - {s['nombre']} ({s['continente']})")
        else:
            print(f"[ERROR] No se encontró ningún país con el nombre '{nombre}'.")
        return False

    pais_encontrado = coincidencias[0]
    print(f"\nPaís seleccionado: {pais_encontrado['nombre']} ({pais_encontrado['continente']})")
    print(f"Valores actuales -> Población: {pais_encontrado['poblacion']:,} hab. | Superficie: {pais_encontrado['superficie']:,} km²")
    
    print("\nIngrese los nuevos datos:")
    nueva_poblacion = validar_entero_positivo("Nueva población (habitantes): ", "Nueva Población")
    nueva_superficie = validar_entero_positivo("Nueva superficie (km²): ", "Nueva Superficie")

    return actualizar_pais(paises, pais_encontrado["nombre"], nueva_poblacion, nueva_superficie)


# Busqueda
def menu_buscar_pais(paises: list[dict]):
    mostrar_titulo("BÚSQUEDA DE PAÍSES POR NOMBRE")
    if not paises:
        print("[AVISO] No hay países registrados.")
        return

    print("Tipo de búsqueda:")
    print("1. Coincidencia Parcial (ej: 'ar' encuentra 'Argentina', 'Marruecos', etc.)")
    print("2. Coincidencia Exacta (ej: 'Brasil')")
    opcion = validar_opcion_menu(["1", "2"], "Seleccione el tipo de búsqueda (1/2): ")

    termino = validar_texto_no_vacio("Ingrese el término de búsqueda: ", "Término")
    es_exacta = (opcion == "2")
    
    resultados = buscar_pais_por_nombre(paises, termino, coincidencia_exacta=es_exacta)
    
    if resultados:
        modo_txt = "exacta" if es_exacta else "parcial"
        mostrar_tabla_paises(resultados, f"Resultados de búsqueda {modo_txt} para '{termino}'")
    else:
        print(f"\n[INFO] No se encontraron países que coincidan con '{termino}'.")


# Filtros
def menu_filtrar_paises(paises: list[dict]):
    mostrar_titulo("FILTRADO DE PAÍSES")
    if not paises:
        print("[AVISO] No hay países registrados.")
        return

    print("Criterios de filtrado disponibles:")
    print("1. Filtrar por Continente")
    print("2. Filtrar por Rango de Población")
    print("3. Filtrar por Rango de Superficie")
    print("0. Volver al menú principal")
    opcion = validar_opcion_menu(["1", "2", "3", "0"], "Seleccione una opción: ")

    filtrados = []
    titulo_tabla = ""

    if opcion == "1":
        continentes = obtener_continentes_unicos(paises)
        print("\nContinentes disponibles:")
        for idx, cont in enumerate(continentes, start=1):
            print(f" {idx}. {cont}")
        nombre_cont = validar_texto_no_vacio("Ingrese el nombre del continente a filtrar: ", "Continente")
        filtrados = filtrar_por_continente(paises, nombre_cont)
        titulo_tabla = f"Países del continente: {nombre_cont.capitalize()}"

    elif opcion == "2":
        min_pob, max_pob = validar_rango_enteros("población", permitir_cero=True)
        filtrados = filtrar_por_rango_poblacion(paises, min_pob, max_pob)
        titulo_tabla = f"Países con población entre {min_pob:,} y {max_pob:,}"

    elif opcion == "3":
        min_sup, max_sup = validar_rango_enteros("superficie en km²", permitir_cero=True)
        filtrados = filtrar_por_rango_superficie(paises, min_sup, max_sup)
        titulo_tabla = f"Países con superficie entre {min_sup:,} km² y {max_sup:,} km²"

    if filtrados:
        mostrar_tabla_paises(filtrados, titulo_tabla)
        print("\n¿Desea ordenar los países filtrados (Ascendente o Descendente)?")
        print("1. Sí, ordenar resultados")
        print("2. No, volver")
        desea_orden = validar_opcion_menu(["1", "2"], "Seleccione una opción (1/2): ")
        if desea_orden == "1":
            menu_ordenar_paises(filtrados)
    elif opcion != "0":
        print("\n[INFO] No se hallaron países que cumplan con el criterio seleccionado.")


# Ordenamiento
def menu_ordenar_paises(paises: list[dict]):
    mostrar_titulo("ORDENAMIENTO DE PAÍSES")
    if not paises:
        print("[AVISO] No hay países para ordenar.")
        return

    print("Seleccione el campo por el cual desea ordenar:")
    print("1. Nombre (Alfabético A-Z / Z-A)")
    print("2. Población (Habitantes)")
    print("3. Superficie / Territorio (km²)")
    print("4. Continente")
    print("0. Cancelar")
    opcion_campo = validar_opcion_menu(["1", "2", "3", "4", "0"], "Seleccione el campo: ")

    if opcion_campo == "0":
        return

    mapa_campos = {
        "1": ("nombre", "Nombre"),
        "2": ("poblacion", "Población"),
        "3": ("superficie", "Superficie / Territorio"),
        "4": ("continente", "Continente")
    }
    clave_campo, nombre_campo = mapa_campos[opcion_campo]

    print("\nSeleccione el sentido del ordenamiento:")
    print("1. Ascendente (A-Z / Menor a Mayor)")
    print("2. Descendente (Z-A / Mayor a Menor)")
    opcion_sentido = validar_opcion_menu(["1", "2"], "Seleccione el sentido: ")
    descendente = (opcion_sentido == "2")

    sentido_txt = "Descendente" if descendente else "Ascendente"
    ordenados = ordenar_paises(paises, clave=clave_campo, descendente=descendente)
    mostrar_tabla_paises(ordenados, f"Países ordenados por {nombre_campo} ({sentido_txt})")


# Estadisticas
def menu_estadisticas(paises: list[dict]):
    if not paises:
        print("\n[ERROR] No hay datos cargados para calcular estadísticas.")
        return
    resumen = generar_resumen_estadistico(paises)
    mostrar_estadisticas_en_consola(resumen)


# Menu principal
def main():
    mostrar_titulo("TRABAJO PRÁCTICO INTEGRADOR: GESTIÓN DE DATOS DE PAÍSES\nTecnicatura Universitaria en Programación - UTN")
    
    paises = cargar_paises_csv(RUTA_CSV_DEFAULT)
    cambios_sin_guardar = False

    while True:
        print("\n" + "=" * 50)
        print("                 MENÚ PRINCIPAL")
        print("=" * 50)
        print(" 1. Listar todos los países")
        print(" 2. Agregar un nuevo país")
        print(" 3. Actualizar datos de un país (Población y Superficie)")
        print(" 4. Buscar país por nombre (parcial o exacta)")
        print(" 5. Filtrar países (por continente, población o superficie)")
        print(" 6. Ordenar países (por nombre, población o superficie)")
        print(" 7. Mostrar estadísticas")
        print(" 8. Guardar cambios en el archivo CSV")
        print(" 9. Recargar dataset desde CSV")
        print(" 0. Salir")
        print("=" * 50)

        if cambios_sin_guardar:
            print("[*] Hay cambios pendientes de guardar en el archivo CSV.")

        opcion = validar_opcion_menu(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            "Seleccione una opción: "
        )

        try:
            if opcion == "1":
                mostrar_tabla_paises(paises, "Listado Completo de Países")
                pausar_consola()

            elif opcion == "2":
                if menu_agregar_pais(paises):
                    cambios_sin_guardar = True
                pausar_consola()

            elif opcion == "3":
                if menu_actualizar_pais(paises):
                    cambios_sin_guardar = True
                pausar_consola()

            elif opcion == "4":
                menu_buscar_pais(paises)
                pausar_consola()

            elif opcion == "5":
                menu_filtrar_paises(paises)
                pausar_consola()

            elif opcion == "6":
                menu_ordenar_paises(paises)
                pausar_consola()

            elif opcion == "7":
                menu_estadisticas(paises)
                pausar_consola()

            elif opcion == "8":
                if guardar_paises_csv(RUTA_CSV_DEFAULT, paises):
                    cambios_sin_guardar = False
                pausar_consola()

            elif opcion == "9":
                if cambios_sin_guardar:
                    confirmacion = validar_opcion_menu(
                        ["s", "n"],
                        "Hay cambios no guardados. ¿Desea descartarlos y recargar? (s/n): "
                    )
                    if confirmacion != "s":
                        print("Operación de recarga cancelada.")
                        pausar_consola()
                        continue
                paises = cargar_paises_csv(RUTA_CSV_DEFAULT)
                cambios_sin_guardar = False
                pausar_consola()

            elif opcion == "0":
                if cambios_sin_guardar:
                    guardar = validar_opcion_menu(
                        ["s", "n"],
                        "¿Desea guardar los cambios en el archivo CSV antes de salir? (s/n): "
                    )
                    if guardar == "s":
                        guardar_paises_csv(RUTA_CSV_DEFAULT, paises)
                print("\n¡Gracias por utilizar el Sistema de Gestión de Países! Hasta luego.\n")
                break

        except Exception as e:
            print(f"\n[ERROR INESPERADO EN LA EJECUCIÓN]: {e}")
            print("El sistema continuará ejecutándose con normalidad.")
            pausar_consola()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma finalizado abruptamente por el usuario.")
