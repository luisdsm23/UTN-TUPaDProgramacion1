# Ejercicio 1: Lista con las notas de 10 estudiantes
# Mostrar la lista completa, calcular el promedio,
# indicar la nota mas alta y la mas baja.

notas_estudiantes = [7, 8, 5, 9, 4, 10, 6, 8, 7, 6]

print(" Notas de los estudiantes ")
for i in range(len(notas_estudiantes)):
    print("Estudiante", i + 1, ":", notas_estudiantes[i])

suma = 0
for i in range(len(notas_estudiantes)):
    suma = suma + notas_estudiantes[i]

promedio = suma / len(notas_estudiantes)

nota_alta = notas_estudiantes[0]
nota_baja  = notas_estudiantes[0]

for i in range(1, len(notas_estudiantes)):
    if notas_estudiantes[i] > nota_alta:
        nota_alta = notas_estudiantes[i]
    if notas_estudiantes[i] < nota_baja:
        nota_baja = notas_estudiantes[i]

print("Promedio general:", promedio)
print("Nota mas alta:", nota_alta)
print("Nota mas baja:", nota_baja)

input("\nPresione Enter o escriba algo para salir...")