# Ejercicio 12: El usuario ingresa 8 numeros enteros.
# Mostrar la lista original, de menor a mayor y de mayor a menor.


lista_numeros_usuario = []

print("\n Ingrese 8 numeros enteros ")
for i in range(8):
    while True:
        entrada = input("Numero " + str(i + 1) + "/8: ")
        if entrada.lstrip("-").isdigit() and entrada != "-":
            lista_numeros_usuario.append(int(entrada))
            break
        print("Ingrese un numero entero valido.")

print("Lista original:")
for i in range(len(lista_numeros_usuario)):
    print(lista_numeros_usuario[i], end=" ")
print()

orden_menor_mayor = sorted(lista_numeros_usuario)
print("De menor a mayor:")
for i in range(len(orden_menor_mayor)):
    print(orden_menor_mayor[i], end=" ")
print()

orden_mayor_menor = sorted(lista_numeros_usuario, reverse=True)
print("De mayor a menor:")
for i in range(len(orden_mayor_menor)):
    print(orden_mayor_menor[i], end=" ")
print()


input("\nPresione Enter o escriba algo para salir...")