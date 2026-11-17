# Ejercicio 11: Lista con 10 estudiantes. Buscar un nombre.
# Indicar si esta en la lista y en que posicion.

lista_nombres = [
    "Agustin", "Belen", "Camila", "Daniel", "Elena",
    "Facundo", "Gabriel", "Ignacio", "Juana", "Lucas"
]

print("\n--- Lista de estudiantes cargados ---")
for i in range(len(lista_nombres)):
    print("  " + str(i + 1) + ". " + lista_nombres[i])

print("\nHay " + str(len(lista_nombres)) + " estudiantes en total.")

print("\n--- Busqueda ---")
nombre_buscado = input("Ingrese el nombre que desea buscar: ")

print("\nBuscando '" + nombre_buscado + "' en la lista...")

encontrado = False
posicion   = -1

for i in range(len(lista_nombres)):
    print("  Revisando posicion " + str(i + 1) + ": " + lista_nombres[i] + "...", end=" ")
    if lista_nombres[i].lower() == nombre_buscado.lower():
        print("ENCONTRADO!")
        encontrado = True
        posicion   = i
        break
    else:
        print("No es.")

print("\n--- Resultado ---")
if encontrado:
    print("El estudiante '" + nombre_buscado + "' SI esta en la lista.")
    print("Lo encontramos en la posicion numero " + str(posicion + 1) + ".")
    print("(Indice interno de la lista: " + str(posicion) + ")")
else:
    print("El estudiante '" + nombre_buscado + "' NO esta en la lista.")
    print("Se revisaron los " + str(len(lista_nombres)) + " estudiantes y no se encontro.")

input("\nPresione Enter o escriba algo para salir...")
