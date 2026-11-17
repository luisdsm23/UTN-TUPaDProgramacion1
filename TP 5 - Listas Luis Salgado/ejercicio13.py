# Ejercicio 13: Lista de puntajes de un videojuego.
# Mostrar el puntaje mas alto y el mas bajo.
# Mostrar el ranking de mayor a menor.
# Indicar en que posicion esta el puntaje 990.


puntajes = [450, 1200, 875, 990, 300, 1500, 640]

print("\n Puntajes del videojuego ")
for i in range(len(puntajes)):
    print(puntajes[i], end=" ")
print()

puntaje_alto = puntajes[0]
puntaje_bajo = puntajes[0]

for i in range(1, len(puntajes)):
    if puntajes[i] > puntaje_alto:
        puntaje_alto = puntajes[i]
    if puntajes[i] < puntaje_bajo:
        puntaje_bajo = puntajes[i]

print("Puntaje mas alto:", puntaje_alto)
print("Puntaje mas bajo:", puntaje_bajo)

ranking = sorted(puntajes, reverse=True)

print("\n--- Ranking ---")
for i in range(len(ranking)):
    print("Puesto " + str(i + 1) + ": " + str(ranking[i]) + " pts")

for i in range(len(ranking)):
    if ranking[i] == 990:
        print("El puntaje 990 esta en el puesto " + str(i + 1) + " del ranking.")
        break

input("\nPresione Enter o escriba algo para salir...")