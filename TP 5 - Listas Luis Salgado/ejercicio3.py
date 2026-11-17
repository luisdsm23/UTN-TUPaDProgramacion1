# Ejercicio 3: Generar 15 numeros al azar entre 1 y 100.
# Crear una lista con los pares y otra con los impares.
# Mostrar cuantos tiene cada lista.

import random

lista_numeros = []
lista_pares   = []
lista_impares = []

for i in range(15):
    n = random.randint(1, 100)
    lista_numeros.append(n)

for i in range(len(lista_numeros)):
    if lista_numeros[i] % 2 == 0:
        lista_pares.append(lista_numeros[i])
    else:
        lista_impares.append(lista_numeros[i])

print("\n Lista original generada ")
for i in range(len(lista_numeros)):
    print(lista_numeros[i], end=" ")
print()

print("Lista de pares (" + str(len(lista_pares)) + " elementos):")
for i in range(len(lista_pares)):
    print(lista_pares[i], end=" ")
print()

print("Lista de impares (" + str(len(lista_impares)) + " elementos):")
for i in range(len(lista_impares)):
    print(lista_impares[i], end=" ")
print()

input("\nPresione Enter o escriba algo para salir...")