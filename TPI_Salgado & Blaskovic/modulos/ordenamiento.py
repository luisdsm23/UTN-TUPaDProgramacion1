from modulos.validaciones import normalizar_texto


CLAVES_VALIDAS = ("nombre", "poblacion", "superficie", "territorio", "continente")


# Extraccion de valor tipado para comparacion
def _obtener_valor_comparacion(pais: dict, clave: str):
    clave_norm = clave.strip().lower()
    if clave_norm == "territorio":
        clave_norm = "superficie"

    if clave_norm == "nombre":
        return normalizar_texto(str(pais.get("nombre", "")))
    elif clave_norm in ("poblacion", "superficie"):
        val = pais.get(clave_norm, 0)
        try:
            return int(val)
        except (ValueError, TypeError):
            return 0
    elif clave_norm == "continente":
        return normalizar_texto(str(pais.get("continente", "")))
    else:
        return pais.get(clave, "")


# Algoritmo de ordenamiento burbuja parametrizable
def ordenar_paises_burbuja(
    paises: list[dict],
    clave: str = "nombre",
    descendente: bool = False
) -> list[dict]:
    """
    Ordena una lista de países aplicando el algoritmo de Bubble Sort (Ordenamiento Burbuja)
    con optimización de bandera (parada temprana si la lista ya está ordenada).

    Parámetros:
      - paises: lista de diccionarios con la información de los países.
      - clave: campo por el cual ordenar ('nombre', 'poblacion', 'superficie'/'territorio', 'continente').
      - descendente: booleano (True para descendente: Z-A / mayor a menor; False para ascendente: A-Z / menor a mayor).
                     También acepta strings como 'desc', 'descendente'.

    Retorna:
      - Nueva lista ordenada sin mutar la lista original.
    """
    if not isinstance(clave, str):
        raise ValueError("La clave de ordenamiento debe ser una cadena de texto.")

    clave_norm = clave.strip().lower()
    if clave_norm == "territorio":
        clave_norm = "superficie"

    if clave_norm not in ("nombre", "poblacion", "superficie", "continente"):
        raise ValueError(
            f"Clave de ordenamiento inválida: '{clave}'. "
            f"Opciones válidas: 'nombre', 'poblacion', 'superficie' (o 'territorio'), 'continente'."
        )

    # Interpretar si descendente viene como string
    es_descendente = descendente
    if isinstance(descendente, str):
        es_descendente = descendente.strip().lower() in ("desc", "descendente", "descending", "true", "1")
    else:
        es_descendente = bool(descendente)

    lista_ordenada = [dict(p) for p in paises]
    n = len(lista_ordenada)

    if n <= 1:
        return lista_ordenada

    for i in range(n):
        hubo_intercambio = False
        for j in range(0, n - i - 1):
            val_a = _obtener_valor_comparacion(lista_ordenada[j], clave_norm)
            val_b = _obtener_valor_comparacion(lista_ordenada[j + 1], clave_norm)

            # Criterio de intercambio según el sentido:
            # Ascendente (A-Z / menor a mayor): si val_a > val_b -> intercambia
            # Descendente (Z-A / mayor a menor): si val_a < val_b -> intercambia
            debe_intercambiar = (val_a < val_b) if es_descendente else (val_a > val_b)

            if debe_intercambiar:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
                hubo_intercambio = True

        # Si en toda la pasada no hubo intercambios, la lista ya está completamente ordenada
        if not hubo_intercambio:
            break

    return lista_ordenada


# Interfaz publica de ordenamiento
def ordenar_paises(
    paises: list[dict],
    clave: str = "nombre",
    descendente: bool = False
) -> list[dict]:
    """Función de interfaz para ordenar la lista de países (ascendente o descendente)."""
    return ordenar_paises_burbuja(paises, clave=clave, descendente=descendente)
