import unicodedata
import re

# Constantes de dominio
CONTINENTES_VALIDOS = ["América", "Europa", "Asia", "África", "Oceanía", "Antártida"]
CLAVES_ORDEN_VALIDAS = ("nombre", "poblacion", "superficie", "territorio", "continente")
SENTIDOS_ORDEN_VALIDOS = ("asc", "desc", "ascending", "descending", "ascendente", "descendente")


# Normalización y utilidades de texto

def normalizar_texto(texto: str) -> str:
    """Elimina acentos/diacríticos y convierte a minúsculas para comparaciones uniformes."""
    if not isinstance(texto, str):
        return ""
    texto_sin_acentos = ''.join(
        c for c in unicodedata.normalize('NFD', texto.strip())
        if unicodedata.category(c) != 'Mn'
    )
    return texto_sin_acentos.lower()


# Validaciones del BACKEND 


def validar_nombre_pais(nombre: str) -> tuple[bool, str, str]:
    """
    Valida el nombre de un país.
    Retorna: (es_valido, nombre_limpio, mensaje_error)
    """
    if nombre is None or not isinstance(nombre, str):
        return False, "", "El nombre del país es obligatorio y debe ser texto."

    limpio = nombre.strip()
    if len(limpio) == 0:
        return False, "", "El nombre del país no puede estar vacío."

    if len(limpio) < 2:
        return False, limpio, "El nombre del país debe tener al menos 2 caracteres."

    if len(limpio) > 70:
        return False, limpio, "El nombre del país no puede superar los 70 caracteres."

    # Permitir letras (incluyendo tildes y diéresis), espacios, guiones y puntos
    # Rechazar números puros o símbolos como @, $, %, etc.
    patron = r"^[A-Za-zÀ-ÿ\u00f1\u00d1\s\.\-\'\’]+$"
    if not re.match(patron, limpio):
        return False, limpio, "El nombre del país solo puede contener letras, espacios, guiones o puntos."

    return True, limpio, ""


def validar_continente(continente: str) -> tuple[bool, str, str]:
    """
    Valida que el continente pertenezca a la lista de continentes reconocidos.
    Retorna: (es_valido, continente_canonico, mensaje_error)
    """
    if continente is None or not isinstance(continente, str):
        return False, "", "El continente es obligatorio y debe ser texto."

    limpio = continente.strip()
    if len(limpio) == 0:
        return False, "", "El continente no puede estar vacío."

    norm = normalizar_texto(limpio)
    for c in CONTINENTES_VALIDOS:
        if normalizar_texto(c) == norm:
            return True, c, ""

    permitidos = ", ".join(CONTINENTES_VALIDOS)
    return False, limpio, f"Continente inválido '{limpio}'. Opciones válidas: {permitidos}."


def validar_entero_positivo_backend(
    valor,
    nombre_campo: str = "Valor",
    permitir_cero: bool = False,
    max_valor: int = None
) -> tuple[bool, int, str]:
    """
    Valida que un valor sea un entero positivo (o cero si se permite).
    Acepta tipos int o strings numéricos enteros.
    Retorna: (es_valido, valor_entero, mensaje_error)
    """
    if valor is None:
        return False, 0, f"El campo '{nombre_campo}' es obligatorio."

    if isinstance(valor, bool):
        return False, 0, f"'{nombre_campo}' no puede ser un valor booleano."

    # Si viene como string
    if isinstance(valor, str):
        val_str = valor.strip()
        if not val_str:
            return False, 0, f"El campo '{nombre_campo}' no puede estar vacío."
        # Rechazar formatos con punto/coma decimal
        if "." in val_str or "," in val_str:
            return False, 0, f"'{nombre_campo}' debe ser un número entero (sin decimales ni separadores de miles)."
        try:
            val_int = int(val_str)
        except ValueError:
            return False, 0, f"'{nombre_campo}' debe ser un número entero válido."
    elif isinstance(valor, (int, float)):
        if isinstance(valor, float) and not valor.is_integer():
            return False, 0, f"'{nombre_campo}' debe ser un número entero sin decimales."
        val_int = int(valor)
    else:
        return False, 0, f"'{nombre_campo}' tiene un tipo de dato inválido."

    minimo = 0 if permitir_cero else 1
    if val_int < minimo:
        limite_msg = "mayor o igual a 0" if permitir_cero else "mayor a 0"
        return False, val_int, f"'{nombre_campo}' debe ser un número entero {limite_msg}."

    if max_valor is not None and val_int > max_valor:
        return False, val_int, f"'{nombre_campo}' no puede superar {max_valor:,}."

    return True, val_int, ""


def validar_datos_nuevo_pais(datos: dict, paises_existentes: list[dict] = None) -> tuple[bool, dict, list[str]]:
    """
    Valida integralmente en el backend los datos para dar de alta un nuevo país.
    Retorna: (es_valido, datos_limpios, lista_errores)
    """
    errores = []
    datos_limpios = {}

    if not isinstance(datos, dict):
        return False, {}, ["El cuerpo de la solicitud debe ser un objeto JSON válido."]

    # 1. Nombre
    val_nom, nom_limpio, err_nom = validar_nombre_pais(datos.get("nombre"))
    if not val_nom:
        errores.append(err_nom)
    else:
        datos_limpios["nombre"] = nom_limpio
        # Verificar duplicado
        if paises_existentes:
            nombre_norm = normalizar_texto(nom_limpio)
            for p in paises_existentes:
                if normalizar_texto(p.get("nombre", "")) == nombre_norm:
                    errores.append(f"El país '{nom_limpio}' ya se encuentra registrado en el sistema.")
                    break

    # 2. Continente
    val_cont, cont_canonico, err_cont = validar_continente(datos.get("continente"))
    if not val_cont:
        errores.append(err_cont)
    else:
        datos_limpios["continente"] = cont_canonico

    # 3. Población (máximo 10 mil millones como cota física razonable)
    val_pob, pob_int, err_pob = validar_entero_positivo_backend(
        datos.get("poblacion"),
        nombre_campo="Población",
        permitir_cero=False,
        max_valor=10_000_000_000
    )
    if not val_pob:
        errores.append(err_pob)
    else:
        datos_limpios["poblacion"] = pob_int

    # 4. Superficie (máximo 510.000.000 km²: superficie total de la Tierra)
    val_sup, sup_int, err_sup = validar_entero_positivo_backend(
        datos.get("superficie"),
        nombre_campo="Superficie",
        permitir_cero=False,
        max_valor=510_000_000
    )
    if not val_sup:
        errores.append(err_sup)
    else:
        datos_limpios["superficie"] = sup_int

    return len(errores) == 0, datos_limpios, errores


def validar_datos_actualizacion_pais(datos: dict, paises_existentes: list[dict] = None) -> tuple[bool, dict, list[str]]:
    """
    Valida en el backend los datos para actualizar población y superficie de un país existente.
    Retorna: (es_valido, datos_limpios, lista_errores)
    """
    errores = []
    datos_limpios = {}

    if not isinstance(datos, dict):
        return False, {}, ["El cuerpo de la solicitud debe ser un objeto JSON válido."]

    # 1. Nombre del país a actualizar
    nombre = datos.get("nombre")
    if not nombre or not isinstance(nombre, str) or not nombre.strip():
        errores.append("El nombre del país es obligatorio para actualizar sus datos.")
    else:
        datos_limpios["nombre"] = nombre.strip()
        if paises_existentes is not None:
            nombre_norm = normalizar_texto(nombre)
            encontrado = any(normalizar_texto(p.get("nombre", "")) == nombre_norm for p in paises_existentes)
            if not encontrado:
                errores.append(f"No se encontró ningún país con el nombre '{nombre.strip()}'.")

    # 2. Nueva Población
    val_pob, pob_int, err_pob = validar_entero_positivo_backend(
        datos.get("poblacion"),
        nombre_campo="Población",
        permitir_cero=False,
        max_valor=10_000_000_000
    )
    if not val_pob:
        errores.append(err_pob)
    else:
        datos_limpios["poblacion"] = pob_int

    # 3. Nueva Superficie
    val_sup, sup_int, err_sup = validar_entero_positivo_backend(
        datos.get("superficie"),
        nombre_campo="Superficie",
        permitir_cero=False,
        max_valor=510_000_000
    )
    if not val_sup:
        errores.append(err_sup)
    else:
        datos_limpios["superficie"] = sup_int

    return len(errores) == 0, datos_limpios, errores


def validar_filtros_query(query: dict) -> tuple[bool, dict, list[str]]:
    """
    Valida en el backend los parámetros de consulta (query params) para filtros y ordenamientos.
    Retorna: (es_valido, filtros_validados, lista_errores)
    """
    errores = []
    filtros = {
        "busqueda": "",
        "exacta": False,
        "continente": "todos",
        "min_pob": None,
        "max_pob": None,
        "min_sup": None,
        "max_sup": None,
        "orden_clave": "nombre",
        "orden_desc": False,
    }

    # Búsqueda por texto
    if "busqueda" in query:
        filtros["busqueda"] = query.get("busqueda", [""])[0].strip()

    # Coincidencia exacta
    if "exacta" in query:
        val_ex = query.get("exacta", ["false"])[0].strip().lower()
        filtros["exacta"] = val_ex in ("true", "1", "si", "yes")

    # Continente
    if "continente" in query:
        cont_val = query.get("continente", ["todos"])[0].strip()
        if cont_val and cont_val.lower() != "todos":
            val_c, c_can, err_c = validar_continente(cont_val)
            if val_c:
                filtros["continente"] = c_can
            else:
                errores.append(err_c)
        else:
            filtros["continente"] = "todos"

    # Rango de Población
    min_pob_raw = query.get("min_pob", [None])[0]
    max_pob_raw = query.get("max_pob", [None])[0]

    if min_pob_raw is not None and str(min_pob_raw).strip() != "":
        ok, val, err = validar_entero_positivo_backend(min_pob_raw, "Población mínima", permitir_cero=True)
        if ok:
            filtros["min_pob"] = val
        else:
            errores.append(err)

    if max_pob_raw is not None and str(max_pob_raw).strip() != "":
        ok, val, err = validar_entero_positivo_backend(max_pob_raw, "Población máxima", permitir_cero=True)
        if ok:
            filtros["max_pob"] = val
        else:
            errores.append(err)

    if filtros["min_pob"] is not None and filtros["max_pob"] is not None:
        if filtros["max_pob"] < filtros["min_pob"]:
            errores.append(
                f"El rango de población es inválido: el valor máximo ({filtros['max_pob']:,}) "
                f"no puede ser menor al mínimo ({filtros['min_pob']:,})."
            )

    # Rango de Superficie
    min_sup_raw = query.get("min_sup", [None])[0]
    max_sup_raw = query.get("max_sup", [None])[0]

    if min_sup_raw is not None and str(min_sup_raw).strip() != "":
        ok, val, err = validar_entero_positivo_backend(min_sup_raw, "Superficie mínima", permitir_cero=True)
        if ok:
            filtros["min_sup"] = val
        else:
            errores.append(err)

    if max_sup_raw is not None and str(max_sup_raw).strip() != "":
        ok, val, err = validar_entero_positivo_backend(max_sup_raw, "Superficie máxima", permitir_cero=True)
        if ok:
            filtros["max_sup"] = val
        else:
            errores.append(err)

    if filtros["min_sup"] is not None and filtros["max_sup"] is not None:
        if filtros["max_sup"] < filtros["min_sup"]:
            errores.append(
                f"El rango de superficie es inválido: el valor máximo ({filtros['max_sup']:,}) "
                f"no puede ser menor al mínimo ({filtros['min_sup']:,})."
            )

    # Clave de Ordenamiento
    orden_clave = query.get("orden_clave", query.get("clave", ["nombre"]))[0].strip().lower()
    if orden_clave == "territorio":
        orden_clave = "superficie"

    if orden_clave in ("nombre", "poblacion", "superficie", "continente"):
        filtros["orden_clave"] = orden_clave
    else:
        errores.append(
            f"Clave de ordenamiento inválida '{orden_clave}'. Opciones permitidas: 'nombre', 'poblacion', 'superficie' (o 'territorio'), 'continente'."
        )

    # Sentido de Ordenamiento (ascendente / descendente)
    sentido_raw = query.get("sentido", query.get("orden_desc", ["false"]))[0].strip().lower()
    if sentido_raw in ("desc", "descending", "descendente", "true", "1"):
        filtros["orden_desc"] = True
    elif sentido_raw in ("asc", "ascending", "ascendente", "false", "0"):
        filtros["orden_desc"] = False
    else:
        errores.append(
            f"Sentido de ordenamiento inválido '{sentido_raw}'. Opciones: 'asc' / 'ascendente' o 'desc' / 'descendente'."
        )

    return len(errores) == 0, filtros, errores


# ==============================================================================
# Validaciones INTERACTIVAS PARA CONSOLA (main.py)
# ==============================================================================

def validar_texto_no_vacio(prompt: str, nombre_campo: str = "Campo") -> str:
    while True:
        try:
            entrada = input(prompt).strip()
            if not entrada:
                print(f"[ERROR] El campo '{nombre_campo}' no puede estar vacío. Intente nuevamente.")
                continue
            return entrada
        except (KeyboardInterrupt, EOFError):
            print("\nOperación cancelada por el usuario.")
            raise


def validar_entero_positivo(prompt: str, nombre_campo: str = "Valor", permitir_cero: bool = False) -> int:
    while True:
        try:
            entrada = input(prompt).strip()
            if not entrada:
                print(f"[ERROR] El campo '{nombre_campo}' es obligatorio. Ingrese un número.")
                continue

            valor = int(entrada)
            minimo = 0 if permitir_cero else 1
            if valor < minimo:
                limite_msg = "mayor o igual a 0" if permitir_cero else "mayor a 0"
                print(f"[ERROR] '{nombre_campo}' debe ser un número entero {limite_msg}.")
                continue
            return valor
        except ValueError:
            print(f"[ERROR] Entrada inválida. '{nombre_campo}' debe ser un número entero sin puntos ni comas.")
        except (KeyboardInterrupt, EOFError):
            print("\nOperación cancelada.")
            raise


def validar_rango_enteros(nombre_campo: str = "valor", permitir_cero: bool = True) -> tuple[int, int]:
    print(f"\n--- Definición de Rango para {nombre_campo.capitalize()} ---")
    minimo = validar_entero_positivo(f"Ingrese {nombre_campo} mínimo: ", f"{nombre_campo} mínimo", permitir_cero=permitir_cero)
    while True:
        maximo = validar_entero_positivo(f"Ingrese {nombre_campo} máximo: ", f"{nombre_campo} máximo", permitir_cero=permitir_cero)
        if maximo < minimo:
            print(f"[ERROR] El valor máximo ({maximo:,}) no puede ser menor al mínimo ({minimo:,}). Reintente.")
            continue
        return minimo, maximo


def validar_opcion_menu(opciones_validas: list[str], prompt: str = "Seleccione una opción: ") -> str:
    while True:
        try:
            seleccion = input(prompt).strip().lower()
            if seleccion in [op.lower() for op in opciones_validas]:
                return seleccion
            print(f"[ERROR] Opción no válida. Las opciones permitidas son: {', '.join(opciones_validas)}.")
        except (KeyboardInterrupt, EOFError):
            print("\nInterrupción detectada.")
            raise
