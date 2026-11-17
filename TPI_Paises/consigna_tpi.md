# TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA - UTN
## Trabajo Práctico Integrador (TPI)
### Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas

---

### Objetivo
Desarrollar una aplicación en Python que permita gestionar información sobre países, aplicando listas, diccionarios, funciones, estructuras condicionales y repetitivas, ordenamientos y estadísticas. El sistema debe ser capaz de leer datos desde un archivo CSV, realizar consultas y generar indicadores clave a partir del dataset. El objetivo principal es afianzar el uso de estructuras de datos, modularización con funciones y técnicas de filtrado/ordenamiento, aplicando los conceptos aprendidos en Programación 1.

---

### Consignas generales
- **Lenguaje:** Python 3.x
- **Estructuras:** listas, diccionarios, funciones.
- **Archivos:** lectura desde CSV.
- **Código:** claro, comentado y modularizado (una función = una responsabilidad).
- **Validaciones:** control de entradas y manejo básico de errores.
- **Modalidad:** Trabajo en equipos de 2 personas.

---

### Dominio (dataset de países)
Cada país estará representado con los siguientes datos:
- `nombre` (string)
- `poblacion` (int)
- `superficie` en km² (int)
- `continente` (string)

#### Ejemplo de registro CSV:
```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

---

### Requerimientos técnicos

#### Diseño (previo al código)
- Explicar en un informe teórico los conceptos aplicados:
  - Listas
  - Diccionarios
  - Funciones
  - Condicionales
  - Ordenamientos
  - Estadísticas básicas
  - Archivos CSV
- Definir el flujo de operaciones principales en un diagrama o esquema.

#### Funcionalidades mínimas del sistema
El programa debe ofrecer un menú de opciones en consola que permita:
1. Agregar un país con todos los datos necesarios para almacenarse (No se permiten campos vacíos).
2. Actualizar los datos de Población y Superficie de un País.
3. Buscar un país por nombre (coincidencia parcial o exacta).
4. Filtrar países por:
   - Continente
   - Rango de población
   - Rango de superficie
5. Ordenar países por:
   - Nombre
   - Población
   - Superficie (ascendente o descendente)
6. Mostrar estadísticas:
   - País con mayor y menor población
   - Promedio de población
   - Promedio de superficie
   - Cantidad de países por continente

#### Validaciones
- Controlar errores de formato en el CSV.
- Evitar fallos al ingresar filtros inválidos o búsquedas sin resultados.
- Mensajes claros de éxito/error.

---

### Entregables (obligatorios)

#### 1. Código Fuente y Datos
- Repositorio en GitHub con el proyecto completo en Python.
- Archivo CSV con el dataset base incluido en el repositorio.
- Archivo `README.md` en la raíz con la descripción del programa, instrucciones de uso, ejemplos de entradas/salidas y participación de los integrantes.

#### 2. Documentación Académica y Técnica (Formato PDF)
El documento debe estar correctamente ordenado, con las hojas numeradas y mantener un formato profesional:
- **Carátula:** Nombre de la institución, carrera, nombre de la materia, título del proyecto, datos de los estudiantes y fecha de entrega.
- **Índice:** Tabla de contenidos estructurada con números de página.
- **Marco Teórico:** Explicación de los conceptos aplicados respaldados con fuentes bibliográficas.
- **Decisiones Técnicas y Arquitectura:** Diagrama de flujo de las operaciones principales y capturas de pantalla de la ejecución de ejemplos.
- **Dificultades y Conclusiones:** Breve apartado con obstáculos técnicos, resolución y reflexiones finales.
- **Bibliografía / Webgrafía:** Enlaces a documentación oficial y recursos de apoyo.
- **Links:** Enlace al repositorio y link al video explicativo.

#### 3. Video Demostración
- Grabación de 10 a 15 minutos mostrando el funcionamiento del sistema en consola.
- Explicación del problema planteado, presentación de la estructura de datos utilizada y demostración del programa con todos sus flujos.

---

### Método de Entrega
La entrega debe realizarse exclusivamente en formato `.zip` conteniendo:
- El código fuente completo desarrollado.
- El documento en formato PDF confeccionado según las consignas establecidas.

En el archivo `README.md` del repositorio se debe incluir obligatoriamente:
- El enlace al video demostrativo con permisos públicos.
- El enlace a la documentación en PDF o el archivo PDF en la raíz del repositorio.
