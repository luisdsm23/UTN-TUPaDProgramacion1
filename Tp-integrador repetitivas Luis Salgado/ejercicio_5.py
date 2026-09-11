# ==============================================================================
# EJERCICIO 5 — “Escape Room: 'La Arena del Gladiador'”
# 1. Descripción del Escenario: Simulador de batalla por turnos contra enemigo.
# ==============================================================================

def ejercicio_5():
    print("\n--- BIENVENIDO A LA ARENA ---")
    
    # Paso 1: Configuración del Personaje
    nombre_gladiador = input("Nombre del Gladiador: ")
    while not nombre_gladiador.isalpha():
        print("Error: Solo se permiten letras.")
        nombre_gladiador = input("Nombre del Gladiador: ")
        
    # Paso 2: Inicialización de Estadísticas (Variables tipadas)
    # String
    gladiador: str = nombre_gladiador
    # Int
    vida_gladiador: int = 100
    vida_enemigo: int = 100
    pociones: int = 3
    dano_base_pesado: int = 15
    dano_base_enemigo: int = 12
    # Boolean
    turno_gladiador: bool = True
    
    print("\n=== INICIO DEL COMBATE ===")
    
    # Paso 3: Ciclo de Combate
    while vida_gladiador > 0 and vida_enemigo > 0:
        if turno_gladiador:
            print(f"\n{gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
            print("Elige acción:")
            print("1. Ataque Pesado")
            print("2. Ráfaga Veloz")
            print("3. Curar")
            
            # Validación de la opción elegida
            opc_str = input("Opción: ")
            while not opc_str.isdigit() or int(opc_str) < 1 or int(opc_str) > 3:
                print("Error: Ingrese un número válido.")
                opc_str = input("Opción: ")
                
            opcion = int(opc_str)
            
            # Acción A: Ataque Pesado (Opción 1)
            if opcion == 1:
                if vida_enemigo < 20:
                    dano_final: float = dano_base_pesado * 1.5  # Cálculo Float
                    print(f"¡GOLPE CRÍTICO! ¡Atacaste al enemigo por {dano_final} puntos de daño!")
                else:
                    dano_final: float = float(dano_base_pesado)
                    print(f"¡Atacaste al enemigo por {int(dano_final)} puntos de daño!")
                    
                vida_enemigo -= int(dano_final)
                if vida_enemigo < 0:
                    vida_enemigo = 0
            
            # Acción B: Ráfaga Veloz (Opción 2)
            elif opcion == 2:
                print(">> ¡Inicias una ráfaga de golpes!")
                # Implementación obligatoria de bucle for usando range
                for golpe in range(3):
                    vida_enemigo -= 5
                    print(" > Golpe conectado por 5 de daño")
                if vida_enemigo < 0:
                    vida_enemigo = 0
            
            # Acción C: Curar (Opción 3)
            elif opcion == 3:
                if pociones > 0:
                    vida_gladiador += 30
                    pociones -= 1
                    print(f"¡Bebiste una poción! Recuperaste 30 HP. Vida actual: {vida_gladiador} | Pociones restantes: {pociones}")
                else:
                    print("¡No quedan pociones!")
            
            # Turno del Enemigo (si el enemigo sigue con vida)
            if vida_enemigo > 0:
                print(f">> ¡El enemigo contraataca por {dano_base_enemigo} puntos!")
                vida_gladiador -= dano_base_enemigo
                if vida_gladiador < 0:
                    vida_gladiador = 0
                print("\n=== NUEVO TURNO ===")
                
    # Paso 4: Fin del Juego
    print("\n" + "="*45)
    if vida_gladiador > 0:
        print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
    else:
        print("DERROTA. Has caído en combate.")
    print("="*45)

if __name__ == "__main__":
    ejercicio_5()
