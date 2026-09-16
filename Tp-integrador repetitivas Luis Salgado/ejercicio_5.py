#5) Ejercicio 5 — “Escape Room: 'La Arena del Gladiador'”
#1. Descripción del Escenario: Simulador de batalla por turnos en Python enfrentando a un Gladiador contra el Enemigo.
#2. Requerimientos Técnicos:
#   - Tipos de Datos: String (nombre jugador), Int (HP y pociones), Float (cálculo de daño ej: crítico multiplica por 1.5), Boolean (control de turno/juego).
#   - Validaciones: Sin try/except. .isalpha() para texto y .isdigit() para números en bucle while.
#3. Flujo del Programa:
#   - Paso 1: Configurar personaje (validar nombre solo letras).
#   - Paso 2: Inicializar vida_jugador=100, vida_enemigo=100, pociones=3, dano_pesado=15, dano_enemigo=12, turno_gladiador=True.
#   - Paso 3: Ciclo mientras ambos tengan > 0 HP:
#     * Turno Jugador: Menú 1. Ataque Pesado (si vida enemigo < 20, golpe crítico x 1.5 en float), 2. Ráfaga Veloz (for de 3 veces restando 5 de vida c/u), 3. Curar (+30 vida, -1 poción si hay).
#     * Turno Enemigo: Ataca restando 12 puntos de daño.
#   - Paso 4: Fin de juego: VICTORIA si vida_jugador > 0, DERROTA si vida_jugador <= 0.

print("X-X BIENVENIDO A LA ARENA X-X")
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# Tipos de datos solicitados:
gladiador = str(nombre)
vida_jugador = int(100)
vida_enemigo = int(100)
pociones = int(3)
dano_pesado = int(15)
dano_enemigo = int(12)
turno_gladiador = bool(True)

print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{gladiador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    opc = input("Opción: ")
    while not opc.isdigit() or int(opc) < 1 or int(opc) > 3:
        print("Ingrese un número válido.")
        opc = input("Opción: ")
    opcion = int(opc)

    if opcion == 1:
        if vida_enemigo < 20:
            dano_critico = float(dano_pesado * 1.5)
            vida_enemigo -= int(dano_critico)
            print(f"¡Atacaste al enemigo por {dano_critico} puntos de daño (Golpe Crítico)!")
        else:
            vida_enemigo -= dano_pesado
            print(f"¡Atacaste al enemigo por {dano_pesado} puntos de daño!")
            
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for _ in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")
            
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f"Te has curado. Vida actual: {vida_jugador} | Pociones restantes: {pociones}")
        else:
            print("¡No quedan pociones!")

    # Turno del enemigo (si todavía sigue vivo)
    if vida_enemigo > 0:
        print(f">> ¡El enemigo contraataca por {dano_enemigo} puntos!")
        vida_jugador -= dano_enemigo
        if vida_jugador > 0:
            print("=== NUEVO TURNO ===")

print("\n" + "="*30)
if vida_jugador > 0:
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
print("="*30)

salir = input("\nMarque 0 para salir de la terminal: ")
while salir != "0":
    salir = input("Marque 0 para salir de la terminal: ")