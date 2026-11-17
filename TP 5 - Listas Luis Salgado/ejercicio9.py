# Ejercicio 9: Tablero de Ta-Te-Ti como lista de listas 3x3.
# Inicializarlo con "-". Dos jugadores ingresan posiciones
# para colocar "X" o "O". Mostrar el tablero tras cada jugada.

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def mostrar_tablero(tab):
    print("  0 1 2")
    for i in range(len(tab)):
        print(str(i) + " ", end="")
        for j in range(len(tab[i])):
            print(tab[i][j], end=" ")
        print()

turno = "X"
jugadas = 0

print("\n Juego de Ta-Te-Ti ")
mostrar_tablero(tablero)

while jugadas < 9:
    print("\nTurno del jugador [" + turno + "]")

    fila_str = input("Ingrese la fila (0, 1 o 2): ")
    col_str  = input("Ingrese la columna (0, 1 o 2): ")

    if not fila_str.isdigit() or not col_str.isdigit():
        print("Ingrese numeros entre 0 y 2.")
        continue

    fila = int(fila_str)
    col  = int(col_str)

    if fila < 0 or fila > 2 or col < 0 or col > 2:
        print("Coordenadas fuera del tablero.")
        continue

    if tablero[fila][col] != "-":
        print("Esa casilla ya esta ocupada.")
        continue

    tablero[fila][col] = turno
    jugadas = jugadas + 1
    mostrar_tablero(tablero)

    if turno == "X":
        turno = "O"
    else:
        turno = "X"

    if jugadas < 9:
        seguir = input("Continuar? (S/N): ").lower()
        if seguir == "n":
            break

print("\nFin del juego.")

input("\nPresione Enter o escriba algo para salir...")