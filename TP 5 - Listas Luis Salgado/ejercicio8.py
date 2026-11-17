# Ejercicio 8: Matriz 5x3 con notas de 5 estudiantes en
# 3 materias. Mostrar el promedio de cada estudiante
# y el promedio de cada materia.

nombres_estudiantes = ["Lucas", "Martina", "Gonzalo", "Sofia", "Julian"]
nombres_materias    = ["Matematica", "Programacion", "Ingles"]

notas_por_estudiante = [
    [8, 9, 7],
    [6, 7, 8],
    [10, 9, 9],
    [4, 6, 5],
    [7, 8, 8]
]

print("\n Promedio por estudiante ")
for i in range(len(notas_por_estudiante)):
    suma = 0
    for j in range(len(notas_por_estudiante[i])):
        suma = suma + notas_por_estudiante[i][j]
    promedio = suma / len(notas_por_estudiante[i])
    print(nombres_estudiantes[i] + ": " + str(promedio))

print("\n Promedio por materia ")
for j in range(len(nombres_materias)):
    suma = 0
    for i in range(len(notas_por_estudiante)):
        suma = suma + notas_por_estudiante[i][j]
    promedio = suma / len(notas_por_estudiante)
    print(nombres_materias[j] + ": " + str(promedio))

input("\nPresione Enter o escriba algo para salir...")