# Pais con mayor poblacion
def pais_mayor_poblacion(paises: list[dict]) -> dict | None:
    if not paises:
        return None

    mayor = paises[0]
    for p in paises[1:]:
        if p.get("poblacion", 0) > mayor.get("poblacion", 0):
            mayor = p
    return mayor


# Pais con menor poblacion
def pais_menor_poblacion(paises: list[dict]) -> dict | None:
    if not paises:
        return None

    menor = paises[0]
    for p in paises[1:]:
        if p.get("poblacion", 0) < menor.get("poblacion", 0):
            menor = p
    return menor


# Promedio de poblacion
def promedio_poblacion(paises: list[dict]) -> float:
    if not paises:
        return 0.0

    suma_poblacion = sum(p.get("poblacion", 0) for p in paises)
    return suma_poblacion / len(paises)


# Promedio de superficie
def promedio_superficie(paises: list[dict]) -> float:
    if not paises:
        return 0.0

    suma_superficie = sum(p.get("superficie", 0) for p in paises)
    return suma_superficie / len(paises)


# Conteo de paises por continente
def cantidad_paises_por_continente(paises: list[dict]) -> dict[str, int]:
    conteo = {}
    for p in paises:
        continente = p.get("continente", "Sin Clasificar").strip()
        if not continente:
            continente = "Sin Clasificar"
        conteo[continente] = conteo.get(continente, 0) + 1
    return conteo


# Resumen estadistico global
def generar_resumen_estadistico(paises: list[dict]) -> dict:
    return {
        "total_paises": len(paises),
        "mayor_poblacion": pais_mayor_poblacion(paises),
        "menor_poblacion": pais_menor_poblacion(paises),
        "promedio_poblacion": promedio_poblacion(paises),
        "promedio_superficie": promedio_superficie(paises),
        "por_continente": cantidad_paises_por_continente(paises)
    }
