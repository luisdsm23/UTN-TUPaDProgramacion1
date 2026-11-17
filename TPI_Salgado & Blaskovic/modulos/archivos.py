import os
import csv


# Carga de paises desde CSV
def cargar_paises_csv(ruta_archivo: str) -> list[dict]:
    paises = []
    
    if not os.path.exists(ruta_archivo):
        print(f"[ADVERTENCIA] El archivo '{ruta_archivo}' no existe aún. Se iniciará con lista vacía.")
        return paises

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8-sig") as archivo:
            lector = csv.reader(archivo)
            
            encabezado = next(lector, None)
            if encabezado is None:
                print(f"[ADVERTENCIA] El archivo '{ruta_archivo}' está completamente vacío.")
                return paises

            encabezado_norm = [col.strip().lower() for col in encabezado]
            columnas_esperadas = ["nombre", "poblacion", "superficie", "continente"]
            
            if len(encabezado_norm) < 4:
                print(f"[ERROR DE FORMATO] El encabezado del CSV no posee las columnas requeridas: {columnas_esperadas}")
                return paises

            linea_num = 1
            registros_corruptos = 0

            for fila in lector:
                linea_num += 1
                
                if not fila or all(campo.strip() == "" for campo in fila):
                    continue

                if len(fila) < 4:
                    print(f"[ERROR DE FORMATO en línea {linea_num}] Columnas insuficientes.")
                    registros_corruptos += 1
                    continue

                nombre = fila[0].strip()
                pob_str = fila[1].strip()
                sup_str = fila[2].strip()
                continente = fila[3].strip()

                if not nombre or not pob_str or not sup_str or not continente:
                    print(f"[ERROR en línea {linea_num}] Campos obligatorios vacíos.")
                    registros_corruptos += 1
                    continue

                try:
                    poblacion = int(pob_str)
                    superficie = int(sup_str)
                except ValueError:
                    print(f"[ERROR DE TIPO en línea {linea_num}] Valores numéricos inválidos.")
                    registros_corruptos += 1
                    continue

                if poblacion < 0 or superficie < 0:
                    print(f"[ERROR DE RANGO en línea {linea_num}] Valores negativos no permitidos.")
                    registros_corruptos += 1
                    continue

                paises.append({
                    "nombre": nombre,
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": continente
                })

            if registros_corruptos > 0:
                print(f"[INFO] Se descartaron {registros_corruptos} registro(s) con formato erróneo.")

        print(f"[ÉXITO] Se cargaron {len(paises)} países correctamente desde '{ruta_archivo}'.")
        return paises

    except PermissionError:
        print(f"[ERROR DE PERMISOS] No tiene permisos para leer el archivo '{ruta_archivo}'.")
        return []
    except Exception as e:
        print(f"[ERROR INESPERADO al leer CSV] {e}")
        return []


# Guardado de paises en CSV
def guardar_paises_csv(ruta_archivo: str, paises: list[dict]) -> bool:
    try:
        directorio = os.path.dirname(ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio, exist_ok=True)

        with open(ruta_archivo, mode="w", encoding="utf-8", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
            
            for p in paises:
                escritor.writerow([
                    p.get("nombre", "").strip(),
                    p.get("poblacion", 0),
                    p.get("superficie", 0),
                    p.get("continente", "").strip()
                ])

        print(f"[ÉXITO] Se guardaron satisfactoriamente {len(paises)} países en '{ruta_archivo}'.")
        return True

    except PermissionError:
        print(f"[ERROR DE PERMISOS] No es posible escribir en '{ruta_archivo}'.")
        return False
    except Exception as e:
        print(f"[ERROR INESPERADO al guardar CSV] {e}")
        return False
