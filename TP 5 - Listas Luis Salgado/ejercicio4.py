# Ejercicio 4: Dada una lista con valores repetidos,
# crear una nueva lista sin elementos repetidos.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []

for i in range(len(datos)):
    if datos[i] not in sin_repetidos:
        sin_repetidos.append(datos[i])

print("\n Lista original ")
for i in range(len(datos)):
    print(datos[i], end=" ")
print()

print("Lista sin repetidos:")
for i in range(len(sin_repetidos)):
    print(sin_repetidos[i], end=" ")
print()

input("\nPresione Enter o escriba algo para salir...")