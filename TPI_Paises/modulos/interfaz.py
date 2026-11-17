def limpiar_pantalla():
    print("\n" + "=" * 80 + "\n")


def pausar_consola(mensaje: str = "\nPresione ENTER para continuar..."):
    try:
        input(mensaje)
    except (EOFError, KeyboardInterrupt):
        pass


def mostrar_titulo(titulo: str):
    ancho = 80
    print("\n" + "=" * ancho)
    print(titulo.center(ancho))
    print("=" * ancho)


# Tabla de paises formateada
def mostrar_tabla_paises(paises: list[dict], titulo: str = "Listado de Países"):
    if not paises:
        print("\n[INFO] No hay países para mostrar con el criterio seleccionado.\n")
        return

    mostrar_titulo(f"{titulo} (Total: {len(paises)})")
    
    ancho_num = 4
    ancho_nom = 24
    ancho_cont = 14
    ancho_pob = 18
    ancho_sup = 18

    linea_divisoria = (
        f"+{'-' * (ancho_num + 2)}"
        f"+{'-' * (ancho_nom + 2)}"
        f"+{'-' * (ancho_cont + 2)}"
        f"+{'-' * (ancho_pob + 2)}"
        f"+{'-' * (ancho_sup + 2)}+"
    )

    encabezado = (
        f"| {'Nº'.center(ancho_num)} "
        f"| {'País'.ljust(ancho_nom)} "
        f"| {'Continente'.ljust(ancho_cont)} "
        f"| {'Población (hab)'.rjust(ancho_pob)} "
        f"| {'Superficie (km²)'.rjust(ancho_sup)} |"
    )

    print(linea_divisoria)
    print(encabezado)
    print(linea_divisoria)

    for idx, p in enumerate(paises, start=1):
        nombre = p.get("nombre", "")[:ancho_nom]
        continente = p.get("continente", "")[:ancho_cont]
        pob_str = f"{p.get('poblacion', 0):,}".replace(",", ".")
        sup_str = f"{p.get('superficie', 0):,}".replace(",", ".")

        fila = (
            f"| {str(idx).rjust(ancho_num)} "
            f"| {nombre.ljust(ancho_nom)} "
            f"| {continente.ljust(ancho_cont)} "
            f"| {pob_str.rjust(ancho_pob)} "
            f"| {sup_str.rjust(ancho_sup)} |"
        )
        print(fila)

    print(linea_divisoria)


# Presentacion de estadisticas
def mostrar_estadisticas_en_consola(resumen: dict):
    mostrar_titulo("ESTADÍSTICAS GENERALES DEL SISTEMA")

    total = resumen.get("total_paises", 0)
    if total == 0:
        print("[AVISO] No se pueden calcular estadísticas porque no hay países registrados.")
        return

    print(f" • Total de países analizados: {total}")
    print("-" * 80)

    mayor = resumen.get("mayor_poblacion")
    menor = resumen.get("menor_poblacion")
    if mayor:
        pob_m = f"{mayor['poblacion']:,}".replace(",", ".")
        print(f" • País con MAYOR población: {mayor['nombre']} ({mayor['continente']}) con {pob_m} habitantes.")
    if menor:
        pob_mn = f"{menor['poblacion']:,}".replace(",", ".")
        print(f" • País con MENOR población: {menor['nombre']} ({menor['continente']}) con {pob_mn} habitantes.")

    print("-" * 80)
    prom_pob = resumen.get("promedio_poblacion", 0.0)
    prom_sup = resumen.get("promedio_superficie", 0.0)
    prom_pob_str = f"{prom_pob:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    prom_sup_str = f"{prom_sup:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    print(f" • Promedio de población:  {prom_pob_str} habitantes por país.")
    print(f" • Promedio de superficie: {prom_sup_str} km² por país.")

    print("-" * 80)
    print(" • Distribución de países por continente:")
    conteo_cont = resumen.get("por_continente", {})
    for continente, cantidad in sorted(conteo_cont.items()):
        porcentaje = (cantidad / total) * 100
        barra = "█" * int(porcentaje / 5)
        print(f"   - {continente.ljust(15)}: {str(cantidad).rjust(3)} país(es) ({porcentaje:5.1f}%)  {barra}")

    print("=" * 80)
