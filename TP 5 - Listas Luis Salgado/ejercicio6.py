# Ejercicio 6: Rotar todos los elementos una posicion
# hacia la derecha (el ultimo pasa a ser el primero).



lista_numeros = [10, 20, 30, 40, 50, 60, 70]

print("\n Lista antes de rotar ")
for i in range(len(lista_numeros)):
    print(lista_numeros[i], end=" ")
print()

ultimo = lista_numeros.pop()
lista_numeros.insert(0, ultimo)

print("Lista despues de rotar a la derecha:")
for i in range(len(lista_numeros)):
    print(lista_numeros[i], end=" ")
print()

input("\nPresione Enter o escriba algo para salir...")