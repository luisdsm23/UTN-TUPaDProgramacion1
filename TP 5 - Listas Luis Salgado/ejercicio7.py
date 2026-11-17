# Ejercicio 7: Matriz 7x2 con temperaturas minimas y maximas
# de una semana. Calcular promedio de minimas y maximas.
# Mostrar el dia con mayor amplitud termica.

dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

temperaturas = [
    [10, 22],
    [12, 25],
    [9,  24],
    [14, 23],
    [11, 21],
    [8,  20],
    [13, 26]
]

suma_minimas = 0
suma_maximas = 0
mayor_amplitud = 0
dia_mayor_amplitud = dias_semana[0]

print("\n Temperaturas de la semana ")
for i in range(len(temperaturas)):
    minima   = temperaturas[i][0]
    maxima   = temperaturas[i][1]
    amplitud = maxima - minima

    suma_minimas = suma_minimas + minima
    suma_maximas = suma_maximas + maxima

    print(dias_semana[i] + ": Min=" + str(minima) + " Max=" + str(maxima) + " Amplitud=" + str(amplitud))

    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias_semana[i]

promedio_minimas = suma_minimas / len(temperaturas)
promedio_maximas = suma_maximas / len(temperaturas)

print("Promedio de minimas:", promedio_minimas)
print("Promedio de maximas:", promedio_maximas)
print("Dia con mayor amplitud termica:", dia_mayor_amplitud, "con", mayor_amplitud, "grados")

input("\nPresione Enter o escriba algo para salir...")