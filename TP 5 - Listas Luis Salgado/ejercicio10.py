# Ejercicio 10: Matriz 4x7 de ventas de 4 productos en 7 dias.
# Mostrar el total vendido por producto.
# Mostrar el dia con mayores ventas totales.
# Indicar el producto mas vendido en la semana.

nombres_productos = ["Chupetin", "Cerveza", "Cigarrillos", "Fideos"]
nombres_dias      = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

ventas_semanales = [
    [10, 15,  8, 12, 20, 25, 30],
    [ 5,  8,  6,  7, 10, 12, 15],
    [20, 22, 18, 25, 30, 35, 40],
    [12, 10, 14, 11, 15, 18, 20]
]

print("\n Total vendido por producto ")
totales_producto = []

for i in range(len(ventas_semanales)):
    total = 0
    for j in range(len(ventas_semanales[i])):
        total = total + ventas_semanales[i][j]
    totales_producto.append(total)
    print("Total de " + nombres_productos[i] + ": " + str(total) + " unidades")

mayor_prod = totales_producto[0]
indice_mayor_prod = 0

for i in range(1, len(totales_producto)):
    if totales_producto[i] > mayor_prod:
        mayor_prod = totales_producto[i]
        indice_mayor_prod = i

print("Producto mas vendido: " + nombres_productos[indice_mayor_prod] + " (" + str(mayor_prod) + " unidades)")

totales_dia = []

for j in range(len(nombres_dias)):
    total_dia = 0
    for i in range(len(ventas_semanales)):
        total_dia = total_dia + ventas_semanales[i][j]
    totales_dia.append(total_dia)

mayor_dia = totales_dia[0]
indice_mayor_dia = 0

for j in range(1, len(totales_dia)):
    if totales_dia[j] > mayor_dia:
        mayor_dia = totales_dia[j]
        indice_mayor_dia = j

print("Dia con mas ventas: " + nombres_dias[indice_mayor_dia] + " (" + str(mayor_dia) + " unidades)")

input("\nPresione Enter o escriba algo para salir...")
