# ==============================================================================
# EJERCICIO 4 — “Escape Room: La Bóveda”
# Historia: Agente intenta abrir una bóveda con 3 cerraduras. Energía y tiempo limitados.
# ==============================================================================

def ejercicio_4():
    print("\n--- EJERCICIO 4: ESCAPE ROOM - LA BÓVEDA ---")
    
    # 1. Validación del nombre del agente
    jugador = input("Nombre del agente: ")
    while not jugador.isalpha():
        print("Solo se permiten letras.")
        jugador = input("Nombre del agente: ")
    
    # Variables iniciales del juego
    energia = 100
    tiempo = 12
    cerraduras_abiertas = 0
    alarma = False
    codigo_parcial = ""
    racha_forzar = 0  # Contador para regla anti-spam
    
    print(f"\n¡Bienvenido Agente {jugador}! Tu misión es abrir las 3 cerraduras de la bóveda.")
    
    # Bucle del juego
    juego_terminado = False
    motivo_fin = ""
    
    while not juego_terminado:
        # Mostrar estado actual
        print("\n" + "-"*40)
        print(f"ESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {'ON' if alarma else 'OFF'} | Código: '{codigo_parcial}'")
        print("ACCIONES:")
        print("1. Forzar cerradura (-20 energía, -2 tiempo)")
        print("2. Hackear panel (-10 energía, -3 tiempo)")
        print("3. Descansar (+15 energía, -1 tiempo)")
        
        opc_str = input("Elige una acción (1-3): ")
        while not opc_str.isdigit() or int(opc_str) < 1 or int(opc_str) > 3:
            print("Seleccione una opción válida (1, 2 o 3).")
            opc_str = input("Elige una acción (1-3): ")
            
        opcion = int(opc_str)
        
        # --- OPCIÓN 1: FORZAR CERRADURA ---
        if opcion == 1:
            racha_forzar += 1
            energia -= 20
            tiempo -= 2
            
            # Regla Anti-spam (3 veces seguidas)
            if racha_forzar == 3:
                alarma = True
                print("¡ANTI-SPAM ACTIVADO! Forzaste la cerradura 3 veces seguidas. La cerradura se trabó y la alarma se activó.")
            else:
                # Riesgo de alarma si la energía está por debajo de 40
                if energia < 40:
                    print("¡ADVERTENCIA: Energía baja! Hay riesgo de alarma.")
                    num_str = input("Elige un número de seguridad (1-3): ")
                    while not num_str.isdigit() or int(num_str) < 1 or int(num_str) > 3:
                        print("Debe ser un número entre 1 y 3.")
                        num_str = input("Elige un número de seguridad (1-3): ")
                    
                    if int(num_str) == 3:
                        alarma = True
                        print("¡Sonó la alarma! Fallaste el intento seguro.")
                
                # Si no hay alarma, abre una cerradura
                if not alarma:
                    cerraduras_abiertas += 1
                    print(f"¡Éxito! Abriste 1 cerradura. Total abiertas: {cerraduras_abiertas}/3.")
                else:
                    print("La alarma está activa. No se pudo abrir la cerradura.")

        # --- OPCIÓN 2: HACKEAR PANEL ---
        elif opcion == 2:
            racha_forzar = 0  # Corta la racha
            energia -= 10
            tiempo -= 3
            
            print("Iniciando secuencia de hackeo...")
            for paso in range(1, 5):
                codigo_parcial += "A"
                print(f" > Hackeando paso {paso}/4... Código parcial: {codigo_parcial}")
            
            if len(codigo_parcial) >= 8:
                if cerraduras_abiertas < 3:
                    cerraduras_abiertas += 1
                    print(f"¡Código completado ({len(codigo_parcial)} caracteres)! Se abrió automáticamente 1 cerradura. Total: {cerraduras_abiertas}/3.")
                else:
                    print("Ya todas las cerraduras estaban abiertas.")

        # --- OPCIÓN 3: DESCANSAR ---
        elif opcion == 3:
            racha_forzar = 0  # Corta la racha
            tiempo -= 1
            if alarma:
                # Si alarma ON: +15 - 10 extra = +5
                energia += 5
                print("Descansaste con la alarma sonando. Recuperaste solo +5 de energía debido al estrés.")
            else:
                energia += 15
                print("Descansaste tranquilamente. Recuperaste +15 de energía.")
            
            # Tope máximo de 100 de energía
            if energia > 100:
                energia = 100

        # Verificación de condiciones de fin de juego
        if cerraduras_abiertas >= 3:
            juego_terminado = True
            motivo_fin = "VICTORIA"
        elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
            juego_terminado = True
            motivo_fin = "DERROTA_BLOQUEO"
        elif energia <= 0 or tiempo <= 0:
            juego_terminado = True
            motivo_fin = "DERROTA_RECURSOS"

    # Mostrar resultado final
    print("\n" + "="*45)
    if motivo_fin == "VICTORIA":
        print(f"¡VICTORIA! ¡Felicitaciones Agente {jugador}, has abierto la bóveda con éxito!")
    elif motivo_fin == "DERROTA_BLOQUEO":
        print("DERROTA. El sistema se bloqueó por la alarma con poco tiempo restante.")
    else:
        print("DERROTA. Te has quedado sin energía o sin tiempo antes de abrir la bóveda.")
    print("="*45)

if __name__ == "__main__":
    ejercicio_4()
