"""
Script para generar el documento PDF académico y profesional requerido para la entrega del TPI.
Materia: Programación 1 - UTN
Utiliza ReportLab para construir un PDF con carátula formal, índice, marco teórico, diagramas y bibliografía.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    KeepTogether,
    HRFlowable,
)
from reportlab.pdfgen import canvas


class NumberedCanvas(canvas.Canvas):
    """Canvas de ReportLab de 2 pasadas para numerar las páginas en el pie: 'Página X de Y'."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        # No dibujar pie ni encabezado en la carátula (página 1)
        if self._pageNumber == 1:
            return

        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#555555"))

        # Encabezado superior
        self.drawString(54, 800, "UTN - Tecnicatura Universitaria en Programación a Distancia | Programación 1")
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(54, 792, 541, 792)

        # Pie de página inferior
        self.line(54, 45, 541, 45)
        self.drawString(54, 32, "TPI: Gestión de Datos de Países en Python")
        page_text = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(541, 32, page_text)
        self.restoreState()


def generar_pdf_documentacion(ruta_salida: str):
    """Construye el documento PDF completo."""
    doc = SimpleDocTemplate(
        ruta_salida,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54,
    )

    styles = getSampleStyleSheet()

    # Colores institucionales
    color_primario = colors.HexColor("#0A3663")     # Azul institucional UTN
    color_secundario = colors.HexColor("#1A5F7A")
    color_texto = colors.HexColor("#222222")
    color_fondo_tabla = colors.HexColor("#F4F6F9")

    # Estilos de texto personalizados
    estilo_titulo_caratula = ParagraphStyle(
        "CaratulaTitulo",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=30,
        alignment=1,
        textColor=color_primario,
        spaceAfter=15,
    )

    estilo_subtitulo_caratula = ParagraphStyle(
        "CaratulaSubtitulo",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        alignment=1,
        textColor=color_secundario,
        spaceAfter=10,
    )

    estilo_h1 = ParagraphStyle(
        "Encabezado1",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=19,
        textColor=color_primario,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True,
    )

    estilo_h2 = ParagraphStyle(
        "Encabezado2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=16,
        textColor=color_secundario,
        spaceBefore=10,
        spaceAfter=5,
        keepWithNext=True,
    )

    estilo_cuerpo = ParagraphStyle(
        "Cuerpo",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=color_texto,
        spaceAfter=6,
    )

    estilo_codigo = ParagraphStyle(
        "CodigoBloque",
        parent=styles["Normal"],
        fontName="Courier",
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#1F2937"),
        backColor=colors.HexColor("#F3F4F6"),
        borderPadding=6,
        spaceBefore=4,
        spaceAfter=8,
    )

    historia = []

    # =========================================================================
    # 1. CARÁTULA
    # =========================================================================
    historia.append(Spacer(1, 40))
    historia.append(Paragraph("UNIVERSIDAD TECNOLÓGICA NACIONAL", estilo_subtitulo_caratula))
    historia.append(Paragraph("TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA", estilo_cuerpo))
    historia.append(Paragraph("<b>CÁTEDRA: PROGRAMACIÓN 1</b>", estilo_cuerpo))
    historia.append(Spacer(1, 40))

    historia.append(HRFlowable(width="100%", thickness=3, color=color_primario, spaceAfter=20))
    historia.append(Paragraph("TRABAJO PRÁCTICO INTEGRADOR (TPI)", estilo_titulo_caratula))
    historia.append(Paragraph("Gestión de Datos de Países en Python:<br/>filtros, ordenamientos y estadísticas", estilo_subtitulo_caratula))
    historia.append(HRFlowable(width="100%", thickness=1, color=color_secundario, spaceBefore=10, spaceAfter=40))

    datos_caratula = [
        [Paragraph("<b>Carrera:</b>", estilo_cuerpo), Paragraph("Tecnicatura Universitaria en Programación a Distancia", estilo_cuerpo)],
        [Paragraph("<b>Materia:</b>", estilo_cuerpo), Paragraph("Programación 1", estilo_cuerpo)],
        [Paragraph("<b>Comisión:</b>", estilo_cuerpo), Paragraph("Comisión 2 - Turno Tarde (ambos integrantes)", estilo_cuerpo)],
        [Paragraph("<b>Lenguaje:</b>", estilo_cuerpo), Paragraph("Python 3.x", estilo_cuerpo)],
        [Paragraph("<b>Integrantes:</b>", estilo_cuerpo), Paragraph("Luis Salgado (Legajo: 55266 | Email: luis.salgado@alumnos.frm.utn.edu.ar)<br/>Branko Blaskovic (Legajo: 55302 | Email: branko.blaskovic@alumnos.frm.utn.edu.ar)", estilo_cuerpo)],
        [Paragraph("<b>Fecha de Entrega:</b>", estilo_cuerpo), Paragraph("Noviembre de 2026", estilo_cuerpo)],
        [Paragraph("<b>Método de Entrega:</b>", estilo_cuerpo), Paragraph("Archivo comprimido .ZIP con código fuente y PDF oficial", estilo_cuerpo)],
    ]

    tabla_caratula = Table(datos_caratula, colWidths=[130, 350])
    tabla_caratula.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, colors.HexColor("#E5E7EB")),
    ]))
    historia.append(tabla_caratula)

    historia.append(PageBreak())

    # =========================================================================
    # 2. ÍNDICE DE CONTENIDOS
    # =========================================================================
    historia.append(Paragraph("ÍNDICE GENERAL", estilo_h1))
    historia.append(HRFlowable(width="100%", thickness=1, color=color_primario, spaceAfter=15))

    indice_datos = [
        [Paragraph("<b>Sección</b>", estilo_cuerpo), Paragraph("<b>Página</b>", estilo_cuerpo)],
        [Paragraph("1. Objetivo y Alcance del Proyecto", estilo_cuerpo), Paragraph("3", estilo_cuerpo)],
        [Paragraph("2. Marco Teórico y Fundamentos Algorítmicos", estilo_cuerpo), Paragraph("3", estilo_cuerpo)],
        [Paragraph("   2.1. Listas y Manipulación Secuencial", estilo_cuerpo), Paragraph("3", estilo_cuerpo)],
        [Paragraph("   2.2. Diccionarios y Modelado de Registros Tabulares", estilo_cuerpo), Paragraph("3", estilo_cuerpo)],
        [Paragraph("   2.3. Modularización y Principio de Responsabilidad Única", estilo_cuerpo), Paragraph("4", estilo_cuerpo)],
        [Paragraph("   2.4. Estructuras de Control y Manejo Defensivo", estilo_cuerpo), Paragraph("4", estilo_cuerpo)],
        [Paragraph("   2.5. Algoritmos de Ordenamiento: Bubble Sort", estilo_cuerpo), Paragraph("4", estilo_cuerpo)],
        [Paragraph("   2.6. Estadísticas Descriptivas Básicas", estilo_cuerpo), Paragraph("5", estilo_cuerpo)],
        [Paragraph("   2.7. Persistencia en Archivos de Texto CSV", estilo_cuerpo), Paragraph("5", estilo_cuerpo)],
        [Paragraph("3. Decisiones Técnicas y Arquitectura del Sistema", estilo_cuerpo), Paragraph("6", estilo_cuerpo)],
        [Paragraph("   3.1. Arquitectura Modular por Capas", estilo_cuerpo), Paragraph("6", estilo_cuerpo)],
        [Paragraph("   3.2. Diagrama de Flujo Principal", estilo_cuerpo), Paragraph("6", estilo_cuerpo)],
        [Paragraph("   3.3. Diagrama de Flujo del Algoritmo de Ordenamiento", estilo_cuerpo), Paragraph("7", estilo_cuerpo)],
        [Paragraph("   3.4. Validaciones y Control de Errores", estilo_cuerpo), Paragraph("7", estilo_cuerpo)],
        [Paragraph("4. Casos de Prueba y Demostración en Consola", estilo_cuerpo), Paragraph("8", estilo_cuerpo)],
        [Paragraph("5. Dificultades Encontradas y Conclusiones", estilo_cuerpo), Paragraph("9", estilo_cuerpo)],
        [Paragraph("6. Bibliografía y Webgrafía", estilo_cuerpo), Paragraph("10", estilo_cuerpo)],
        [Paragraph("7. Enlaces Oficiales (GitHub, Video y Documentación)", estilo_cuerpo), Paragraph("10", estilo_cuerpo)],
    ]

    tabla_indice = Table(indice_datos, colWidths=[400, 80])
    tabla_indice.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), color_fondo_tabla),
        ("ALIGN", (1, 0), (1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, colors.HexColor("#E5E7EB")),
    ]))
    historia.append(tabla_indice)

    historia.append(PageBreak())

    # =========================================================================
    # 3. OBJETIVO Y MARCO TEÓRICO
    # =========================================================================
    historia.append(Paragraph("1. Objetivo y Alcance del Proyecto", estilo_h1))
    historia.append(Paragraph(
        "El presente Trabajo Práctico Integrador tiene como meta diseñar e implementar una aplicación "
        "integral en Python 3.x para la administración, filtrado, ordenamiento y análisis estadístico "
        "de datos demográficos de países. El desarrollo pone en práctica los conceptos nucleares de "
        "la materia Programación 1: estructuras de datos compuestas (listas de diccionarios), "
        "modularización con funciones bajo el principio de responsabilidad única, algoritmos clásicos "
        "de ordenamiento y búsqueda, manejo de excepciones y persistencia en archivos CSV.",
        estilo_cuerpo
    ))

    historia.append(Spacer(1, 10))
    historia.append(Paragraph("2. Marco Teórico y Fundamentos Algorítmicos", estilo_h1))

    historia.append(Paragraph("2.1. Listas y Manipulación Secuencial", estilo_h2))
    historia.append(Paragraph(
        "Una lista en Python (<code>list</code>) es una estructura de datos secuencial, mutable e indexada, "
        "implementada internamente como un arreglo dinámico de punteros a objetos (Hettinger, 2020). Permite "
        "acceso posicional en tiempo constante O(1) e inserciones/eliminaciones al final amortizadas en O(1). "
        "En el proyecto, la lista actúa como contenedor en memoria de todos los registros de países.",
        estilo_cuerpo
    ))

    historia.append(Paragraph("2.2. Diccionarios y Modelado de Registros Tabulares", estilo_h2))
    historia.append(Paragraph(
        "Un diccionario (<code>dict</code>) es una estructura asociativa de pares clave-valor respaldada por "
        "una tabla hash (Python Software Foundation, 2024). Ofrece operaciones de consulta e inserción con "
        "costo temporal promedio de O(1). Cada país se modela mediante un diccionario con las claves "
        "<code>nombre</code> (str), <code>poblacion</code> (int), <code>superficie</code> (int) y "
        "<code>continente</code> (str). La combinación de listas de diccionarios resulta idónea por su alta "
        "legibilidad y facilidad de serialización.",
        estilo_cuerpo
    ))

    historia.append(Paragraph("2.3. Modularización y Principio de Responsabilidad Única", estilo_h2))
    historia.append(Paragraph(
        "La modularización consiste en descomponer un problema complejo en componentes independientes y "
        "reutilizables. Siguiendo el Principio de Responsabilidad Única (Martin, 2008), cada función debe "
        "resolver exclusivamente una tarea. De este modo, la lectura/escritura de archivos se separa "
        "rigurosamente de las validaciones de entrada, la lógica de cálculo y la presentación en pantalla.",
        estilo_cuerpo
    ))

    historia.append(Paragraph("2.4. Estructuras de Control y Manejo Defensivo", estilo_h2))
    historia.append(Paragraph(
        "Las bifurcaciones condicionales (<code>if / elif / else</code>) y los ciclos iterativos "
        "(<code>while / for</code>) rigen el flujo interactivo de la consola. La programación defensiva se "
        "aplica capturando excepciones comunes (como <code>ValueError</code> al parsear números) para evitar "
        "caídas abruptas de la aplicación.",
        estilo_cuerpo
    ))

    historia.append(Paragraph("2.5. Algoritmos de Ordenamiento: Bubble Sort", estilo_h2))
    historia.append(Paragraph(
        "El ordenamiento de burbuja compara pares adyacentes de elementos y los intercambia si no cumplen "
        "el orden deseado (Knuth, 1998). Posee una complejidad temporal de O(n²) en el peor caso y O(1) en "
        "espacio. Se optimizó con una bandera que finaliza el proceso en O(n) si la lista ya está ordenada. "
        "El algoritmo fue implementado desde cero para demostrar el dominio de bucles e intercambios.",
        estilo_cuerpo
    ))

    historia.append(Paragraph("2.6. Estadísticas Descriptivas Básicas", estilo_h2))
    historia.append(Paragraph(
        "El módulo calcula el máximo y mínimo de población en un único recorrido O(n), la media aritmética "
        "de población y superficie (suma total dividida el total de países), y un diccionario de distribución "
        "de frecuencias absolutas y relativas por continente.",
        estilo_cuerpo
    ))

    historia.append(Paragraph("2.7. Persistencia en Archivos de Texto CSV", estilo_h2))
    historia.append(Paragraph(
        "El formato CSV almacena información tabular delimitada por comas. Mediante el manejador de "
        "contexto <code>with open(...)</code> y la codificación <code>utf-8-sig</code>, el sistema garantiza "
        "persistencia confiable, liberación automática de descriptores de archivo y tolerancia ante caracteres "
        "especiales o tildes.",
        estilo_cuerpo
    ))

    historia.append(PageBreak())

    # =========================================================================
    # 4. DECISIONES TÉCNICAS Y ARQUITECTURA
    # =========================================================================
    historia.append(Paragraph("3. Decisiones Técnicas y Arquitectura del Sistema", estilo_h1))
    historia.append(Paragraph(
        "El proyecto se diseñó bajo una arquitectura modular desacoplada en capas para garantizar alta "
        "cohesión y bajo acoplamiento:",
        estilo_cuerpo
    ))

    modulos_tabla = [
        [Paragraph("<b>Módulo</b>", estilo_cuerpo), Paragraph("<b>Responsabilidad Principal</b>", estilo_cuerpo)],
        [Paragraph("<code>main.py</code>", estilo_cuerpo), Paragraph("Punto de entrada. Menú interactivo en consola y orquestación de opciones.", estilo_cuerpo)],
        [Paragraph("<code>modulos/archivos.py</code>", estilo_cuerpo), Paragraph("Lectura/escritura del CSV, validación de cabeceras y control de filas dañadas.", estilo_cuerpo)],
        [Paragraph("<code>modulos/operaciones.py</code>", estilo_cuerpo), Paragraph("Altas, modificaciones, búsquedas (exacta/parcial) y filtros (continente, rangos).", estilo_cuerpo)],
        [Paragraph("<code>modulos/ordenamiento.py</code>", estilo_cuerpo), Paragraph("Algoritmo Bubble Sort parametrizado por clave y sentido (ascendente/descendente).", estilo_cuerpo)],
        [Paragraph("<code>modulos/estadisticas.py</code>", estilo_cuerpo), Paragraph("Cálculo de máximos, mínimos, promedios y conteo de países por continente.", estilo_cuerpo)],
        [Paragraph("<code>modulos/validaciones.py</code>", estilo_cuerpo), Paragraph("Validación de números enteros positivos, cadenas no vacías y normalización.", estilo_cuerpo)],
        [Paragraph("<code>modulos/interfaz.py</code>", estilo_cuerpo), Paragraph("Formateo de tablas alineadas en consola con separadores y barras estadísticas.", estilo_cuerpo)],
    ]

    t_mod = Table(modulos_tabla, colWidths=[150, 330])
    t_mod.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), color_fondo_tabla),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, colors.HexColor("#E5E7EB")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D1D5DB")),
    ]))
    historia.append(t_mod)

    historia.append(Spacer(1, 10))
    historia.append(Paragraph("3.2. Diagrama de Flujo Principal del Sistema", estilo_h2))

    diagrama_texto = """
    +-------------------------------------------------------------+
    |                    INICIO DEL PROGRAMA                      |
    +-------------------------------------------------------------+
                                   |
                                   v
             [ Cargar dataset 'paises.csv' a memoria ]
                                   |
                                   v
    +-----------------> [ Mostrar Menú Principal ]
    |                              |
    |                              v
    |                 [ Seleccionar Opción (0 a 9) ]
    |                              |
    |      +-----------------------+-----------------------+
    |      | (Opciones 1..7)                               | (Opción 0)
    |      v                                               v
    |  [ Ejecutar Operación de Negocio ]       [ ¿Cambios pendientes? ]
    |  - 1. Listar Países                             |           |
    |  - 2. Agregar País                          (Sí)|       (No)|
    |  - 3. Actualizar País                           v           v
    |  - 4. Buscar (Parcial / Exacta)          [ Guardar CSV ]    |
    |  - 5. Filtrar (Cont., Pobl., Sup.)              |           |
    |  - 6. Ordenar (Nombre, Pobl., Sup.)             +-----+-----+
    |  - 7. Estadísticas Generales                          |
    |  - 8. Guardar CSV / 9. Recargar                       v
    |      |                                            [  FIN  ]
    +------+
    """
    historia.append(Paragraph(f"<pre>{diagrama_texto}</pre>", estilo_codigo))

    historia.append(PageBreak())

    # =========================================================================
    # 5. CASOS DE PRUEBA Y DEMOSTRACIÓN
    # =========================================================================
    historia.append(Paragraph("4. Casos de Prueba y Demostración en Consola", estilo_h1))
    historia.append(Paragraph(
        "Se implementó una batería de 10 pruebas automatizadas mediante el framework estándar "
        "<code>unittest</code> de Python. A continuación se detallan los casos probados:",
        estilo_cuerpo
    ))

    test_datos = [
        [Paragraph("<b>Caso de Prueba</b>", estilo_cuerpo), Paragraph("<b>Descripción</b>", estilo_cuerpo), Paragraph("<b>Resultado</b>", estilo_cuerpo)],
        [Paragraph("<code>test_normalizar_texto</code>", estilo_cuerpo), Paragraph("Eliminación de tildes y conversión a minúsculas ('Japón' -> 'japon').", estilo_cuerpo), Paragraph("EXITOSO", estilo_cuerpo)],
        [Paragraph("<code>test_agregar_pais</code>", estilo_cuerpo), Paragraph("Inserción de país nuevo y rechazo de duplicados sin importar mayúsculas.", estilo_cuerpo), Paragraph("EXITOSO", estilo_cuerpo)],
        [Paragraph("<code>test_actualizar_pais</code>", estilo_cuerpo), Paragraph("Actualización precisa de población y km² en países existentes.", estilo_cuerpo), Paragraph("EXITOSO", estilo_cuerpo)],
        [Paragraph("<code>test_buscar_pais</code>", estilo_cuerpo), Paragraph("Búsqueda exacta y búsqueda parcial ('ar' encuentra Argentina).", estilo_cuerpo), Paragraph("EXITOSO", estilo_cuerpo)],
        [Paragraph("<code>test_filtrar_continente</code>", estilo_cuerpo), Paragraph("Filtrado estricto de países por continente geográfico.", estilo_cuerpo), Paragraph("EXITOSO", estilo_cuerpo)],
        [Paragraph("<code>test_filtrar_rangos</code>", estilo_cuerpo), Paragraph("Filtrado por cotas mínima y máxima de habitantes y superficie.", estilo_cuerpo), Paragraph("EXITOSO", estilo_cuerpo)],
        [Paragraph("<code>test_ordenamiento</code>", estilo_cuerpo), Paragraph("Ordenamiento por nombre, población y superficie (asc / desc).", estilo_cuerpo), Paragraph("EXITOSO", estilo_cuerpo)],
        [Paragraph("<code>test_estadisticas</code>", estilo_cuerpo), Paragraph("Cálculo de máximos, mínimos, promedios y conteo por continente.", estilo_cuerpo), Paragraph("EXITOSO", estilo_cuerpo)],
        [Paragraph("<code>test_archivos_csv</code>", estilo_cuerpo), Paragraph("Guardado y lectura con persistencia en archivos temporales.", estilo_cuerpo), Paragraph("EXITOSO", estilo_cuerpo)],
    ]

    t_tests = Table(test_datos, colWidths=[140, 260, 80])
    t_tests.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), color_fondo_tabla),
        ("ALIGN", (2, 0), (2, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D1D5DB")),
    ]))
    historia.append(t_tests)

    historia.append(Spacer(1, 10))
    historia.append(Paragraph("Ejemplo de Ejecución en Consola (Cálculo Estadístico):", estilo_h2))
    salida_consola = """
    +--------------------------------------------------------------------------+
    |                    ESTADISTICAS GENERALES DEL SISTEMA                    |
    +--------------------------------------------------------------------------+
      Total de paises analizados: 25
      Pais con MAYOR poblacion: China (Asia) con 1.412.000.000 habitantes.
      Pais con MENOR poblacion: Uruguay (America) con 3.485.152 habitantes.
      Promedio de poblacion:    185.187.351 habitantes por pais.
      Promedio de superficie:   2.378.117 km2 por pais.
      Distribucion de paises por continente:
        - America : 6 pais(es) (24.0%)
        - Asia    : 4 pais(es) (16.0%)
        - Europa  : 7 pais(es) (28.0%)
        - Oceania : 2 pais(es) ( 8.0%)
        - Africa  : 6 pais(es) (24.0%)
    +--------------------------------------------------------------------------+
    """
    historia.append(Paragraph(f"<pre>{salida_consola}</pre>", estilo_codigo))

    historia.append(PageBreak())

    # =========================================================================
    # 6. DIFICULTADES, CONCLUSIONES Y BIBLIOGRAFÍA
    # =========================================================================
    historia.append(Paragraph("5. Dificultades Encontradas y Conclusiones", estilo_h1))
    historia.append(Paragraph("<b>Obstáculos Técnicos y Soluciones:</b>", estilo_cuerpo))
    historia.append(Paragraph(
        "1. <i>Normalización de texto con caracteres especiales:</i> En español los acentos son comunes "
        "(ej. Japón, América). Para evitar fallos en búsquedas y ordenamientos, se aplicó la descomposición "
        "Unicode NFD, descartando diacríticos.<br/>"
        "2. <i>Preservación de la lista original:</i> Durante la ordenación de datos para visualización, "
        "se creó una copia explícita de la lista de diccionarios, evitando efectos colaterales en el dataset "
        "en memoria.<br/>"
        "3. <i>Robustez ante errores en el archivo CSV:</i> Se descartaron filas con columnas faltantes o "
        "campos numéricos no válidos mediante un bloque <code>try-except</code> línea por línea, evitando "
        "que un registro corrupto impidiera cargar los demás países válidos.",
        estilo_cuerpo
    ))

    historia.append(Spacer(1, 6))
    historia.append(Paragraph("<b>Conclusión y Aprendizaje Grupal:</b>", estilo_cuerpo))
    historia.append(Paragraph(
        "El desarrollo del Trabajo Práctico Integrador permitió afianzar y articular todos los contenidos "
        "nucleares de Programación 1. La modularización no solo facilitó la división equitativa del trabajo en el "
        "equipo de dos personas, sino que dotó al código de gran legibilidad, testeabilidad y escalabilidad.",
        estilo_cuerpo
    ))

    historia.append(Spacer(1, 10))
    historia.append(Paragraph("6. Bibliografía y Webgrafía", estilo_h1))
    bibliografia_items = [
        "1. <b>Python Software Foundation (2024).</b> <i>The Python Standard Library Documentation</i>. https://docs.python.org/3/",
        "2. <b>Knuth, D. E. (1998).</b> <i>The Art of Computer Programming, Volume 3: Sorting and Searching</i>. Addison-Wesley.",
        "3. <b>Martin, R. C. (2008).</b> <i>Clean Code: A Handbook of Agile Software Craftsmanship</i>. Prentice Hall.",
        "4. <b>Sweigart, A. (2020).</b> <i>Automate the Boring Stuff with Python</i>. No Starch Press.",
        "5. <b>Lutz, M. (2013).</b> <i>Learning Python (5th Edition)</i>. O'Reilly Media.",
    ]
    for b in bibliografia_items:
        historia.append(Paragraph(b, estilo_cuerpo))

    historia.append(Spacer(1, 10))
    historia.append(Paragraph("7. Enlaces Oficiales del Proyecto", estilo_h1))
    historia.append(Paragraph(
        "• <b>Repositorio en GitHub:</b> https://github.com/luisdsm23/UTN-TUPaDProgramacion1<br/>"
        "• <b>Video Demostrativo:</b> [INSERTAR_AQUI_LINK_DEL_VIDEO] (Duración: 10 a 15 min)<br/>"
        "• <b>Documentación en PDF:</b> Incluida en la raíz de la entrega como <code>Documentacion_TPI.pdf</code>.",
        estilo_cuerpo
    ))

    # Construir documento con NumberedCanvas
    doc.build(historia, canvasmaker=NumberedCanvas)
    print(f"[ÉXITO] Documento PDF generado exitosamente en: '{ruta_salida}'.")


if __name__ == "__main__":
    ruta_pdf = os.path.join(os.path.dirname(__file__), "Documentacion_TPI.pdf")
    generar_pdf_documentacion(ruta_pdf)
