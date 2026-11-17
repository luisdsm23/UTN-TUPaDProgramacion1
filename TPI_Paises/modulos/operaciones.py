from modulos.validaciones import normalizar_texto


# Verificacion de existencia
def existe_pais(paises: list[dict], nombre: str) -> bool:
    nombre_norm = normalizar_texto(nombre)
    for p in paises:
        if normalizar_texto(p.get("nombre", "")) == nombre_norm:
            return True
    return False


# Alta de pais
def agregar_pais(paises: list[dict], nombre: str, poblacion: int, superficie: int, continente: str) -> bool:
    if not nombre or not continente:
        print("[ERROR] El nombre y el continente son obligatorios y no pueden estar vacíos.")
        return False

    if poblacion <= 0 or superficie <= 0:
        print("[ERROR] La población y la superficie deben ser enteros mayores a 0.")
        return False

    if existe_pais(paises, nombre):
        print(f"[ERROR] El país '{nombre}' ya se encuentra registrado en el sistema.")
        return False

    nuevo_pais = {
        "nombre": nombre.strip(),
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente.strip()
    }
    paises.append(nuevo_pais)
    print(f"[ÉXITO] País '{nuevo_pais['nombre']}' agregado exitosamente.")
    return True


# Actualizacion de datos de pais
def actualizar_pais(paises: list[dict], nombre: str, nueva_poblacion: int, nueva_superficie: int) -> bool:
    if nueva_poblacion <= 0 or nueva_superficie <= 0:
        print("[ERROR] Los nuevos valores de población y superficie deben ser mayores a 0.")
        return False

    nombre_norm = normalizar_texto(nombre)
    for p in paises:
        if normalizar_texto(p.get("nombre", "")) == nombre_norm:
            poblacion_anterior = p["poblacion"]
            superficie_anterior = p["superficie"]
            p["poblacion"] = nueva_poblacion
            p["superficie"] = nueva_superficie
            print(f"[ÉXITO] Datos de '{p['nombre']}' actualizados:")
            print(f"  - Población: {poblacion_anterior:,} -> {nueva_poblacion:,}")
            print(f"  - Superficie: {superficie_anterior:,} km² -> {nueva_superficie:,} km²")
            return True

    print(f"[ERROR] No se encontró el país '{nombre}' para actualizar.")
    return False


# Busqueda por nombre
def buscar_pais_por_nombre(paises: list[dict], termino: str, coincidencia_exacta: bool = False) -> list[dict]:
    termino_norm = normalizar_texto(termino)
    if not termino_norm:
        return []

    resultados = []
    for p in paises:
        nombre_norm = normalizar_texto(p.get("nombre", ""))
        if coincidencia_exacta:
            if nombre_norm == termino_norm:
                resultados.append(p)
        else:
            if termino_norm in nombre_norm:
                resultados.append(p)

    return resultados


# Filtro por continente
def filtrar_por_continente(paises: list[dict], continente: str) -> list[dict]:
    cont_norm = normalizar_texto(continente)
    return [p for p in paises if normalizar_texto(p.get("continente", "")) == cont_norm]


# Filtro por rango de poblacion
def filtrar_por_rango_poblacion(paises: list[dict], min_pob: int, max_pob: int) -> list[dict]:
    return [p for p in paises if min_pob <= p.get("poblacion", 0) <= max_pob]


# Filtro por rango de superficie
def filtrar_por_rango_superficie(paises: list[dict], min_sup: int, max_sup: int) -> list[dict]:
    return [p for p in paises if min_sup <= p.get("superficie", 0) <= max_sup]


# Obtencion de continentes unicos
def obtener_continentes_unicos(paises: list[dict]) -> list[str]:
    continentes = set()
    for p in paises:
        cont = p.get("continente", "").strip()
        if cont:
            continentes.add(cont)
    return sorted(list(continentes))
