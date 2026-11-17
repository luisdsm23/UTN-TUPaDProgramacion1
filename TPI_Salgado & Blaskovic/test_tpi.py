"""
Suite de pruebas automatizadas para verificar el correcto funcionamiento del TPI.
Materia: Programación 1 - UTN
"""

import unittest
import os
import sys
import tempfile

DIR_RAIZ = os.path.dirname(os.path.abspath(__file__))
if DIR_RAIZ not in sys.path:
    sys.path.insert(0, DIR_RAIZ)

from modulos.validaciones import (
    normalizar_texto,
    validar_nombre_pais,
    validar_continente,
    validar_entero_positivo_backend,
    validar_datos_nuevo_pais,
    validar_datos_actualizacion_pais,
    validar_filtros_query,
)
from modulos.archivos import cargar_paises_csv, guardar_paises_csv
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
from modulos.estadisticas import (
    pais_mayor_poblacion,
    pais_menor_poblacion,
    promedio_poblacion,
    promedio_superficie,
    cantidad_paises_por_continente,
)


class TestTPIPaises(unittest.TestCase):

    def setUp(self):
        self.dataset_prueba = [
            {"nombre": "Argentina", "poblacion": 45376763, "superficie": 2780400, "continente": "América"},
            {"nombre": "Japón", "poblacion": 125800000, "superficie": 377975, "continente": "Asia"},
            {"nombre": "Brasil", "poblacion": 213993437, "superficie": 8515767, "continente": "América"},
            {"nombre": "Alemania", "poblacion": 83149300, "superficie": 357022, "continente": "Europa"},
        ]

    def test_normalizar_texto(self):
        self.assertEqual(normalizar_texto("  Japón  "), "japon")
        self.assertEqual(normalizar_texto("América"), "america")
        self.assertEqual(normalizar_texto("Álvaro"), "alvaro")

    def test_validaciones_backend_individuales(self):
        # 1. Nombre
        ok, nom, err = validar_nombre_pais("Canadá")
        self.assertTrue(ok)
        self.assertEqual(nom, "Canadá")

        ok, _, err = validar_nombre_pais("   ")
        self.assertFalse(ok)
        self.assertIn("vacío", err)

        ok, _, err = validar_nombre_pais("País123$")
        self.assertFalse(ok)
        self.assertIn("solo puede contener letras", err)

        # 2. Continente
        ok, cont, err = validar_continente("america")
        self.assertTrue(ok)
        self.assertEqual(cont, "América")

        ok, _, err = validar_continente("Atlantis")
        self.assertFalse(ok)
        self.assertIn("inválido", err)

        # 3. Entero positivo
        ok, val, err = validar_entero_positivo_backend("50000", "Población")
        self.assertTrue(ok)
        self.assertEqual(val, 50000)

        ok, _, err = validar_entero_positivo_backend("-10", "Población")
        self.assertFalse(ok)

        ok, _, err = validar_entero_positivo_backend("15.5", "Población")
        self.assertFalse(ok)

    def test_validaciones_backend_nuevo_pais(self):
        # Alta válida
        datos_ok = {
            "nombre": "Uruguay",
            "continente": "América",
            "poblacion": 3485152,
            "superficie": 176215
        }
        valido, limpios, errores = validar_datos_nuevo_pais(datos_ok, self.dataset_prueba)
        self.assertTrue(valido)
        self.assertEqual(len(errores), 0)
        self.assertEqual(limpios["nombre"], "Uruguay")

        # Duplicado
        datos_dup = {
            "nombre": "argentina",
            "continente": "América",
            "poblacion": 45000000,
            "superficie": 2780400
        }
        valido, _, errores = validar_datos_nuevo_pais(datos_dup, self.dataset_prueba)
        self.assertFalse(valido)
        self.assertTrue(any("ya se encuentra registrado" in e for e in errores))

        # Múltiples errores juntos
        datos_malos = {
            "nombre": "",
            "continente": "ContinenteFalso",
            "poblacion": -50,
            "superficie": "invalido"
        }
        valido, _, errores = validar_datos_nuevo_pais(datos_malos, self.dataset_prueba)
        self.assertFalse(valido)
        self.assertGreaterEqual(len(errores), 3)

    def test_validaciones_backend_actualizar_pais(self):
        # Actualización válida
        datos_act = {
            "nombre": "Argentina",
            "poblacion": 46000000,
            "superficie": 2780450
        }
        valido, limpios, errores = validar_datos_actualizacion_pais(datos_act, self.dataset_prueba)
        self.assertTrue(valido)
        self.assertEqual(limpios["poblacion"], 46000000)

        # País inexistente
        datos_inex = {
            "nombre": "Narnia",
            "poblacion": 1000,
            "superficie": 1000
        }
        valido, _, errores = validar_datos_actualizacion_pais(datos_inex, self.dataset_prueba)
        self.assertFalse(valido)
        self.assertTrue(any("No se encontró" in e for e in errores))

    def test_validaciones_backend_query_filtros(self):
        # Query válida con orden ascendente
        q_ok = {
            "continente": ["Europa"],
            "min_pob": ["1000000"],
            "max_pob": ["100000000"],
            "clave": ["superficie"],
            "sentido": ["ascendente"]
        }
        valido, filtros, errores = validar_filtros_query(q_ok)
        self.assertTrue(valido)
        self.assertEqual(filtros["continente"], "Europa")
        self.assertEqual(filtros["orden_clave"], "superficie")
        self.assertFalse(filtros["orden_desc"])  # False = ascendente

        # Rango inválido (max < min)
        q_rango_malo = {
            "min_pob": ["500"],
            "max_pob": ["200"]
        }
        valido, _, errores = validar_filtros_query(q_rango_malo)
        self.assertFalse(valido)
        self.assertTrue(any("no puede ser menor" in e for e in errores))

        # Clave inválida
        q_clave_mala = {"clave": ["edad"]}
        valido, _, errores = validar_filtros_query(q_clave_mala)
        self.assertFalse(valido)

    def test_agregar_pais_exito_y_duplicado(self):
        lista = list(self.dataset_prueba)
        res = agregar_pais(lista, "Chile", 19000000, 756000, "América")
        self.assertTrue(res)
        self.assertEqual(len(lista), 5)

        res_dup = agregar_pais(lista, "chile", 20000000, 800000, "América")
        self.assertFalse(res_dup)
        self.assertEqual(len(lista), 5)

    def test_agregar_pais_invalido(self):
        lista = list(self.dataset_prueba)
        self.assertFalse(agregar_pais(lista, "PaísX", 0, 1000, "Europa"))
        self.assertFalse(agregar_pais(lista, "", 1000, 1000, "Europa"))

    def test_actualizar_pais(self):
        lista = [dict(p) for p in self.dataset_prueba]
        res = actualizar_pais(lista, "argentina", 46000000, 2780450)
        self.assertTrue(res)
        self.assertEqual(lista[0]["poblacion"], 46000000)
        self.assertEqual(lista[0]["superficie"], 2780450)

        res_inexistente = actualizar_pais(lista, "Atlantida", 1000, 1000)
        self.assertFalse(res_inexistente)

    def test_buscar_pais(self):
        res_ex = buscar_pais_por_nombre(self.dataset_prueba, "japon", coincidencia_exacta=True)
        self.assertEqual(len(res_ex), 1)
        self.assertEqual(res_ex[0]["nombre"], "Japón")

        res_parcial = buscar_pais_por_nombre(self.dataset_prueba, "ar", coincidencia_exacta=False)
        nombres = [p["nombre"] for p in res_parcial]
        self.assertIn("Argentina", nombres)

    def test_filtrar_por_continente(self):
        res = filtrar_por_continente(self.dataset_prueba, "america")
        self.assertEqual(len(res), 2)
        for p in res:
            self.assertEqual(p["continente"], "América")

    def test_filtrar_por_rangos(self):
        res_pob = filtrar_por_rango_poblacion(self.dataset_prueba, 50000000, 100000000)
        self.assertEqual(len(res_pob), 1)
        self.assertEqual(res_pob[0]["nombre"], "Alemania")

        res_sup = filtrar_por_rango_superficie(self.dataset_prueba, 300000, 400000)
        self.assertEqual(len(res_sup), 2)

    def test_ordenamiento_completo_ascendente_descendente(self):
        # 1. Nombre: Ascendente (A-Z) y Descendente (Z-A)
        ord_nom_asc = ordenar_paises(self.dataset_prueba, "nombre", descendente=False)
        self.assertEqual([p["nombre"] for p in ord_nom_asc], ["Alemania", "Argentina", "Brasil", "Japón"])

        ord_nom_desc = ordenar_paises(self.dataset_prueba, "nombre", descendente=True)
        self.assertEqual([p["nombre"] for p in ord_nom_desc], ["Japón", "Brasil", "Argentina", "Alemania"])

        # 2. Población: Ascendente (menor a mayor) y Descendente (mayor a menor)
        ord_pob_asc = ordenar_paises(self.dataset_prueba, "poblacion", descendente=False)
        self.assertEqual(ord_pob_asc[0]["nombre"], "Argentina")  # ~45M
        self.assertEqual(ord_pob_asc[-1]["nombre"], "Brasil")     # ~213M

        ord_pob_desc = ordenar_paises(self.dataset_prueba, "poblacion", descendente=True)
        self.assertEqual(ord_pob_desc[0]["nombre"], "Brasil")
        self.assertEqual(ord_pob_desc[-1]["nombre"], "Argentina")

        # 3. Superficie / Territorio: Ascendente y Descendente
        ord_sup_asc = ordenar_paises(self.dataset_prueba, "superficie", descendente=False)
        self.assertEqual(ord_sup_asc[0]["nombre"], "Alemania")  # 357.022 km²
        self.assertEqual(ord_sup_asc[-1]["nombre"], "Brasil")    # 8.515.767 km²

        # Acepta alias "territorio"
        ord_ter_desc = ordenar_paises(self.dataset_prueba, "territorio", descendente=True)
        self.assertEqual(ord_ter_desc[0]["nombre"], "Brasil")
        self.assertEqual(ord_ter_desc[-1]["nombre"], "Alemania")

        # 4. Continente: Ascendente y Descendente
        ord_cont_asc = ordenar_paises(self.dataset_prueba, "continente", descendente=False)
        continentes_orden = [p["continente"] for p in ord_cont_asc]
        # América, América, Asia, Europa
        self.assertEqual(continentes_orden, ["América", "América", "Asia", "Europa"])

    def test_estadisticas(self):
        mayor = pais_mayor_poblacion(self.dataset_prueba)
        self.assertEqual(mayor["nombre"], "Brasil")

        menor = pais_menor_poblacion(self.dataset_prueba)
        self.assertEqual(menor["nombre"], "Argentina")

        prom_p = promedio_poblacion(self.dataset_prueba)
        self.assertAlmostEqual(prom_p, (45376763 + 125800000 + 213993437 + 83149300) / 4)

        conteos = cantidad_paises_por_continente(self.dataset_prueba)
        self.assertEqual(conteos["América"], 2)
        self.assertEqual(conteos["Asia"], 1)
        self.assertEqual(conteos["Europa"], 1)

    def test_guardar_y_cargar_csv(self):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            tmp_path = tmp.name

        try:
            exito = guardar_paises_csv(tmp_path, self.dataset_prueba)
            self.assertTrue(exito)

            cargados = cargar_paises_csv(tmp_path)
            self.assertEqual(len(cargados), len(self.dataset_prueba))
            self.assertEqual(cargados[0]["nombre"], "Argentina")
            self.assertEqual(cargados[0]["poblacion"], 45376763)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)


if __name__ == "__main__":
    unittest.main()
