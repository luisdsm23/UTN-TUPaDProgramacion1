# Ejercicio 5: Lista de 8 estudiantes presentes.
# Preguntar si se quiere agregar uno nuevo o eliminar uno.
# Mostrar la lista final actualizada.


lista_estudiantes = ["Lucas", "Martina", "Gonzalo", "Sofia",
                     "Julian", "Camila", "Agustin", "Valeria"]

print("\n Estudiantes presentes ")
for i in range(len(lista_estudiantes)):
    print(str(i + 1) + ".", lista_estudiantes[i])

print("1. Agregar un estudiante")
print("2. Eliminar un estudiante")
opcion = input("Elija una opcion (1 o 2): ")

while opcion != "1" and opcion != "2":
    print("Opcion invalida. Ingrese 1 o 2.")
    opcion = input("Elija una opcion (1 o 2): ")

if opcion == "1":
    nuevo_estudiante = input("Nombre del nuevo estudiante: ")
    lista_estudiantes.append(nuevo_estudiante)
    print("Estudiante agregado.")
elif opcion == "2":
    nombre_eliminar = input("Nombre del estudiante a eliminar: ")
    if nombre_eliminar in lista_estudiantes:
        lista_estudiantes.remove(nombre_eliminar)
        print("Estudiante eliminado.")
    else:
        print("Ese estudiante no esta en la lista.")

print("Lista actualizada:")
for i in range(len(lista_estudiantes)):
    print(str(i + 1) + ".", lista_estudiantes[i])

input("\nPresione Enter o escriba algo para salir...")
