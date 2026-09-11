# ==============================================================================
# TRABAJO PRÁCTICO 5: LISTAS
# ALUMNO: Luis Salgado
# MATERIA: Programación 1 - Tecnicatura Universitaria en Programación (UTN)
# NOTA: Siempre que se pide mostrar una lista o sus elementos, se utilizan estructuras repetitivas.
# ==============================================================================

#1) Crear una lista con las notas de 10 estudiantes.
#● Mostrar la lista completa.
#● Calcular y mostrar el promedio.
#● Indicar la nota más alta y la más baja.

notas = [7.5, 8.0, 6.5, 9.0, 4.0, 10.0, 5.5, 8.5, 7.0, 6.0]

print("--- NOTAS DE LOS 10 ESTUDIANTES ---")
print("Lista de notas:")
for i in range(len(notas)):
    print(f"Estudiante {i + 1}: {notas[i]}")

suma_notas = 0
for n in notas:
    suma_notas += n

promedio = suma_notas / len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)

print(f"\nPromedio general: {promedio:.2f}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")

#En este ejercicio defini una lista con 10 valores flotantes que representan las notas. Use un ciclo for con range(len(notas)) para recorrer e imprimir cada nota en pantalla cumpliendo la pauta de usar estructuras repetitivas. Para calcular el promedio sume todas las notas iterando con for y dividi por la cantidad total con len(), y finalmente use las funciones max() y min() para obtener la calificacion mas alta y mas baja.


#2) Pedir al usuario que cargue 5 productos en una lista.
#● Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#● Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []
print("\n--- CARGA DE 5 PRODUCTOS ---")
for i in range(5):
    prod = input(f"Ingrese el nombre del producto {i + 1}: ")
    while prod.strip() == "":
        print("Error: El nombre del producto no puede estar vacío.")
        prod = input(f"Ingrese el nombre del producto {i + 1}: ")
    productos.append(prod)

productos_ordenados = sorted(productos)

print("\nLista de productos ordenada alfabéticamente:")
for p in productos_ordenados:
    print(f"- {p}")

prod_eliminar = input("\nIngrese el nombre del producto que desea eliminar: ")
if prod_eliminar in productos:
    productos.remove(prod_eliminar)
    print(f"El producto '{prod_eliminar}' ha sido eliminado exitosamente.")
else:
    print(f"El producto '{prod_eliminar}' no se encuentra en la lista.")

print("\nLista de productos actualizada:")
for p in productos:
    print(f"- {p}")

#Aca inicialice una lista vacia llamada productos y use un for para pedirle 5 elementos al usuario con .append(). Use sorted() para generar una copia ordenada alfabeticamente sin alterar la lista original al mostrarla. Luego le consulte al usuario que producto queria quitar, comprobe su existencia con el operador 'in' y lo elimine usando .remove(), mostrando la lista final con otro bucle for.


#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#● Crear una lista con los pares y otra con los impares.
#● Mostrar cuántos números tiene cada lista.

import random

numeros_azar = []
for _ in range(15):
    numeros_azar.append(random.randint(1, 100))

pares = []
impares = []

for num in numeros_azar:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("\n--- NÚMEROS AL AZAR ---")
print("Lista original generada:")
for n in numeros_azar:
    print(n, end=" ")
print()

print(f"\nLista de números pares ({len(pares)} elementos):")
for p in pares:
    print(p, end=" ")
print()

print(f"\nLista de números impares ({len(impares)} elementos):")
for imp in impares:
    print(imp, end=" ")
print()

#Importe la libreria random y use randint(1, 100) dentro de un for para generar 15 numeros aleatorios. Despues recorri la lista evaluando con el operador modulo (%) si el resto al dividir por 2 daba 0 para agregarlo a la lista de pares o al else para impares con .append(). Con len() mostre la cantidad de elementos de cada una.


#4) Dada una lista con valores repetidos: datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
#● Crear una nueva lista sin elementos repetidos.
#● Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []

for elemento in datos:
    if elemento not in sin_repetidos:
        sin_repetidos.append(elemento)

print("\n--- ELIMINACIÓN DE REPETIDOS ---")
print("Lista original:")
for d in datos:
    print(d, end=" ")
print()

print("Lista sin repetidos:")
for sr in sin_repetidos:
    print(sr, end=" ")
print()

#Tome la lista con datos duplicados y cree una nueva lista vacia llamada sin_repetidos. Recorri la lista original con un for y use la condicion 'if elemento not in sin_repetidos' para asegurarme de agregar cada numero solo la primera vez que aparece, conservando los valores unicos y mostrandolos con un ciclo for.


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#● Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#● Mostrar la lista final actualizada.

estudiantes = ["Lucas", "Martina", "Gonzalo", "Sofia", "Julian", "Camila", "Agustin", "Valeria"]

print("\n--- ESTUDIANTES PRESENTES EN CLASE ---")
print("Lista inicial de presentes:")
for est in estudiantes:
    print(f"- {est}")

print("\n¿Qué acción desea realizar?")
print("1. Agregar un nuevo estudiante")
print("2. Eliminar un estudiante existente")
opcion = input("Elija una opción (1 o 2): ")

while opcion != "1" and opcion != "2":
    print("Opción inválida. Ingrese 1 o 2.")
    opcion = input("Elija una opción (1 o 2): ")

if opcion == "1":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"Estudiante '{nuevo}' agregado con éxito.")
elif opcion == "2":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print(f"Estudiante '{eliminar}' eliminado de la lista.")
    else:
        print(f"El estudiante '{eliminar}' no se encontraba en la lista.")

print("\nLista final actualizada de estudiantes:")
for est in estudiantes:
    print(f"- {est}")

#Cree una lista inicial de 8 estudiantes y mostre a todos con un bucle for. Le di un menu simple de dos opciones al usuario para agregar mediante .append() o eliminar mediante .remove() (validando previamente con 'in' si el estudiante figuraba en la lista para evitar errores). Finalmente mostre la lista actualizada recorriendola con otro for.


#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

numeros_rotar = [10, 20, 30, 40, 50, 60, 70]

print("\n--- ROTACIÓN DE ELEMENTOS ---")
print("Lista antes de la rotación:")
for n in numeros_rotar:
    print(n, end=" ")
print()

# El último elemento pasa al principio:
ultimo_elemento = numeros_rotar.pop()
numeros_rotar.insert(0, ultimo_elemento)

print("Lista luego de rotar 1 posición a la derecha:")
for n in numeros_rotar:
    print(n, end=" ")
print()

#Para rotar la lista a la derecha use el metodo .pop() sin argumentos, el cual extrae y devuelve el ultimo elemento de la lista. Luego utilice el metodo .insert(0, ultimo_elemento) para insertarlo exactamente en la primera posicion (indice 0), desplazando todos los demas elementos hacia la derecha.


#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
#● Calcular el promedio de las mínimas y el de las máximas.
#● Mostrar en qué día se registró la mayor amplitud térmica.

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
# Cada fila representa [temperatura_minima, temperatura_maxima]
temperaturas = [
    [10.5, 22.0],  # Lunes
    [12.0, 25.5],  # Martes
    [9.0, 24.0],   # Miércoles (amplitud = 15.0)
    [14.0, 23.0],  # Jueves
    [11.5, 21.0],  # Viernes
    [8.0, 20.0],   # Sábado
    [13.0, 26.0]   # Domingo
]

print("\n--- REGISTRO DE TEMPERATURAS SEMANALES (7x2) ---")
suma_minimas = 0
suma_maximas = 0
mayor_amplitud = 0
dia_mayor_amplitud = ""

for i in range(len(temperaturas)):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]
    amplitud = maxima - minima
    
    suma_minimas += minima
    suma_maximas += maxima
    
    print(f"{dias_semana[i]}: Mínima = {minima}°C | Máxima = {maxima}°C | Amplitud = {amplitud:.1f}°C")
    
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias_semana[i]

promedio_minimas = suma_minimas / len(temperaturas)
promedio_maximas = suma_maximas / len(temperaturas)

print(f"\nPromedio de temperaturas mínimas: {promedio_minimas:.2f}°C")
print(f"Promedio de temperaturas máximas: {promedio_maximas:.2f}°C")
print(f"Mayor amplitud térmica: {dia_mayor_amplitud} con {mayor_amplitud:.1f}°C de diferencia.")

#Cree una matriz de 7 filas y 2 columnas con listas anidadas donde el indice 0 es la minima y el indice 1 es la maxima. Recorri las 7 filas con un ciclo for, acumulando las minimas y maximas para calcular sus promedios, y calculando la amplitud (maxima - minima) en cada dia para guardar con un if el dia y valor con mayor diferencia termica.


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#● Mostrar el promedio de cada estudiante.
#● Mostrar el promedio de cada materia.

estudiantes_nombres = ["Alumno 1", "Alumno 2", "Alumno 3", "Alumno 4", "Alumno 5"]
materias_nombres = ["Matemática", "Programación", "Inglés"]

# Matriz 5x3 (5 filas de estudiantes, 3 columnas de notas por materia)
matriz_notas = [
    [8, 9, 7],   # Alumno 1
    [6, 7, 8],   # Alumno 2
    [10, 10, 9], # Alumno 3
    [4, 6, 5],   # Alumno 4
    [7, 8, 8]    # Alumno 5
]

print("\n--- NOTAS DE 5 ESTUDIANTES EN 3 MATERIAS ---")
print("Promedio por estudiante:")
for i in range(len(matriz_notas)):
    suma_estudiante = 0
    for j in range(len(matriz_notas[i])):
        suma_estudiante += matriz_notas[i][j]
    promedio_estudiante = suma_estudiante / len(matriz_notas[i])
    print(f"- {estudiantes_nombres[i]}: {promedio_estudiante:.2f}")

print("\nPromedio por materia:")
for j in range(len(materias_nombres)):
    suma_materia = 0
    for i in range(len(matriz_notas)):
        suma_materia += matriz_notas[i][j]
    promedio_materia = suma_materia / len(matriz_notas)
    print(f"- {materias_nombres[j]}: {promedio_materia:.2f}")

#Defini una matriz de 5x3. Para obtener el promedio por estudiante recorri las filas calculando la suma de sus 3 materias. Para el promedio por materia inverti los indices del bucle anidado (fijando la columna j y recorriendo las filas i) para sumar las notas de todos los estudiantes en cada materia y dividirlas por 5.


#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#● Inicializarlo con guiones "-" representando casillas vacías.
#● Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#● Mostrar el tablero después de cada jugada.

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def mostrar_tablero(tab):
    print("  0 1 2")
    for idx, fila in enumerate(tab):
        print(f"{idx} " + " ".join(fila))

print("\n--- JUEGO DE TA-TE-TI (3x3) ---")
mostrar_tablero(tablero)

jugadas = 0
turno = "X"

while jugadas < 9:
    print(f"\nTurno del Jugador ({turno}):")
    f_str = input("Ingrese fila (0, 1, 2): ")
    c_str = input("Ingrese columna (0, 1, 2): ")
    
    if not (f_str.isdigit() and c_str.isdigit()):
        print("Error: Debe ingresar números del 0 al 2.")
        continue
        
    fila = int(f_str)
    col = int(c_str)
    
    if fila < 0 or fila > 2 or col < 0 or col > 2:
        print("Error: Posición fuera del tablero.")
        continue
        
    if tablero[fila][col] != "-":
        print("Error: Esa casilla ya está ocupada.")
        continue
        
    tablero[fila][col] = turno
    jugadas += 1
    mostrar_tablero(tablero)
    
    # Alternar turno entre X y O
    if turno == "X":
        turno = "O"
    else:
        turno = "X"
        
    # Preguntamos si desean continuar otra jugada de prueba o terminar
    if jugadas < 9:
        seguir = input("¿Desea realizar otra jugada? (S/N): ").lower()
        if seguir == "n":
            break

print("Fin de la demostración del Ta-Te-Ti.")

#Represente el tablero mediante una lista de 3 listas con "-" para casillas vacias. Cree un bucle que le pide la fila y columna a cada jugador, valida que las coordenadas esten entre 0 y 2 y que la casilla este desocupada. Se actualiza la posicion en tablero[fila][col] con 'X' o 'O' y se vuelve a dibujar el tablero con ciclos for.


#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#● Mostrar el total vendido por cada producto.
#● Mostrar el día con mayores ventas totales.
#● Indicar cuál fue el producto más vendido en la semana.

productos_tienda = ["Producto A", "Producto B", "Producto C", "Producto D"]
dias_semana_ventas = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Matriz 4x7 (4 filas de productos x 7 columnas de días)
ventas = [
    [10, 15, 8, 12, 20, 25, 30],  # Producto A
    [5,  8,  6, 7,  10, 12, 15],  # Producto B
    [20, 22, 18, 25, 30, 35, 40], # Producto C
    [12, 10, 14, 11, 15, 18, 20]  # Producto D
]

print("\n--- VENTAS DE LA TIENDA (4x7) ---")
totales_por_producto = []
for i in range(len(ventas)):
    total_prod = 0
    for j in range(len(ventas[i])):
        total_prod += ventas[i][j]
    totales_por_producto.append(total_prod)
    print(f"Total vendido de {productos_tienda[i]}: {total_prod} unidades")

# Producto más vendido
max_unidades_prod = max(totales_por_producto)
indice_mas_vendido = totales_por_producto.index(max_unidades_prod)
print(f"\nEl producto más vendido en la semana fue: {productos_tienda[indice_mas_vendido]} ({max_unidades_prod} unidades)")

# Día con mayores ventas totales
totales_por_dia = []
for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    totales_por_dia.append(total_dia)

max_ventas_dia = max(totales_por_dia)
indice_dia_max = totales_por_dia.index(max_ventas_dia)
print(f"El día con mayores ventas totales fue: {dias_semana_ventas[indice_dia_max]} ({max_ventas_dia} unidades)")

#Cree una matriz de 4x7. Sume las filas para obtener el acumulado vendido por cada producto y determine el mayor con max() e index(). Luego sume las columnas fijando el dia j para calcular las ventas diarias totales de los 4 articulos y encontrar que dia de la semana tuvo el mayor volumen de venta.


#11) Crear una lista con los nombres de 10 estudiantes.
#● Solicitar al usuario que ingrese un nombre a buscar.
#● Indicar si el nombre se encuentra en la lista.
#● Mostrar la posición en la que aparece.
#● Si no se encuentra, informar que no está en la lista.

estudiantes_lista = [
    "Agustin", "Belen", "Camila", "Daniel", "Elena", 
    "Facundo", "Gabriel", "Ignacio", "Juana", "Lucas"
]

print("\n--- BÚSQUEDA DE ESTUDIANTE EN LISTA ---")
print("Nombres cargados:")
for nombre in estudiantes_lista:
    print(f"- {nombre}")

buscado = input("\nIngrese el nombre del estudiante a buscar: ")

encontrado = False
posicion = -1

for i in range(len(estudiantes_lista)):
    if estudiantes_lista[i].lower() == buscado.lower():
        encontrado = True
        posicion = i
        break

if encontrado:
    print(f"El estudiante '{buscado}' se encuentra en la lista en la posición {posicion} (Índice {posicion}).")
else:
    print(f"El estudiante '{buscado}' NO se encuentra en la lista.")

#Cree una lista con 10 nombres de estudiantes. Recorri la lista con un bucle for y la funcion len() comparando en minusculas (.lower()) cada elemento con el texto ingresado. Si coincide, guarde su indice en una variable y corte la busqueda con break para luego mostrar la posicion exacta, o imprimir el mensaje de que no existe en caso de no hallarlo.


#12) Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
#● Mostrar la lista original.
#● Mostrar la lista ordenada de menor a mayor.
#● Mostrar la lista ordenada de mayor a menor.
#● Investigar el uso de sorted() y del parámetro reverse.

numeros_usuario = []
print("\n--- INGRESO DE 8 NÚMEROS ENTEROS ---")
for i in range(8):
    num_str = input(f"Ingrese el número entero {i + 1}/8: ")
    while not num_str.lstrip("-").isdigit() or num_str.strip() == "":
        print("Error: Debe ingresar un número entero válido.")
        num_str = input(f"Ingrese el número entero {i + 1}/8: ")
    numeros_usuario.append(int(num_str))

print("\nLista original:")
for n in numeros_usuario:
    print(n, end=" ")
print()

# Ordenada de menor a mayor con sorted()
menor_a_mayor = sorted(numeros_usuario)
print("\nLista ordenada de menor a mayor:")
for n in menor_a_mayor:
    print(n, end=" ")
print()

# Ordenada de mayor a menor con sorted(..., reverse=True)
mayor_a_menor = sorted(numeros_usuario, reverse=True)
print("\nLista ordenada de mayor a menor (reverse=True):")
for n in mayor_a_menor:
    print(n, end=" ")
print()

#Cargue 8 numeros enteros validados en una lista mediante un for. Utilice la funcion sorted(lista) para obtener una nueva lista ordenada ascendentemente (de menor a mayor), y sorted(lista, reverse=True) activando el parametro reverse para ordenarla de forma descendente (de mayor a menor), mostrando cada una con bucles repetitivos for.


#13) Dada la siguiente lista de puntajes de un videojuego:
#puntajes = [450, 1200, 875, 990, 300, 1500, 640]
#● Mostrar el puntaje más alto y el más bajo.
#● Mostrar la lista ordenada de mayor a menor (ranking).
#● Indicar en qué posición del ranking se encuentra el puntaje 990.

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

print("\n--- PUNTAJES DE VIDEOJUEGO ---")
print("Puntajes registrados:")
for p in puntajes:
    print(p, end=" ")
print()

puntaje_max = max(puntajes)
puntaje_min = min(puntajes)

print(f"\nPuntaje más alto: {puntaje_max}")
print(f"Puntaje más bajo: {puntaje_min}")

ranking = sorted(puntajes, reverse=True)

print("\nRanking de puntajes (ordenado de mayor a menor):")
for puesto, score in enumerate(ranking, start=1):
    print(f"Puesto {puesto}: {score} pts")

posicion_990 = ranking.index(990) + 1
print(f"\nEl puntaje 990 se encuentra en la posición {posicion_990} del ranking.")

#A partir de la lista dada, use max() y min() para los extremos de puntaje. Cree el ranking ordenando con sorted(puntajes, reverse=True). Mostre el listado con un for usando enumerate() comenzando en 1 para indicar los puestos, y finalmente obtuve la posicion del puntaje 990 utilizando ranking.index(990) + 1.
