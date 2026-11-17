# Ejercicio 2: Cargar 5 productos, mostrar ordenados
# alfabeticamente, preguntar cual eliminar y mostrar
# la lista actualizada.

lista_productos = []

print("\n Ingrese 5 productos ")
for i in range(5):
    producto = input("Ingrese el producto " + str(i + 1) + ": ")
    lista_productos.append(producto)

productos_ordenados = sorted(lista_productos)

print("Lista ordenada alfabeticamente:")
for i in range(len(productos_ordenados)):
    print("-", productos_ordenados[i])

producto_eliminar = input("Que producto desea eliminar? ")

if producto_eliminar in lista_productos:
    lista_productos.remove(producto_eliminar)
    print("Producto eliminado correctamente.")
else:
    print("Ese producto no se encuentra en la lista.")

print("Lista actualizada:")
for i in range(len(lista_productos)):
    print("-", lista_productos[i])

input("\nPresione Enter o escriba algo para salir...")