#4) Ejercicio 4 — “Escape Room: La Bóveda”
#Historia: Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados. Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.
#Variables iniciales (NO se piden por teclado):
#energia = 100, tiempo = 12, cerraduras_abiertas = 0, alarma = False, codigo_parcial = ""
#Validaciones obligatorias: No usar try/except. Pedir nombre del agente y validar con .isalpha() en un while. Validar opciones del menú con .isdigit() en un while.
#Regla anti-spam: Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas: se cobra el costo normal (-20 energía, -2 tiempo), NO abre cerradura y se activa la alarma automáticamente (alarma = True). Si elige opción 2 o 3 se corta la racha.
#Menú de acciones:
#1. Forzar cerradura (-20 energía, -2 tiempo): Si energía < 40 riesgo de alarma (pedir número 1-3 validado, si elige 3 alarma=True). Si no hay alarma abre 1 cerradura.
#2. Hackear panel (-10 energía, -3 tiempo): Usar for de 4 pasos mostrando progreso. En cada paso sumar letra a codigo_parcial. Si len(codigo_parcial) >= 8 abre automáticamente 1 cerradura si faltan.
#3. Descansar (+15 energía máx 100, -1 tiempo; si alarma ON: -10 energía extra).
#Regla de bloqueo por alarma: Si alarma == True y tiempo <= 3 y no abrió la bóveda, sistema se bloquea y se pierde.
#Condiciones de fin: cerraduras == 3 -> VICTORIA / energia <= 0 o tiempo <= 0 -> DERROTA / bloqueo por alarma -> DERROTA.

jugador = input("Nombre del agente: ")
while not jugador.isalpha():
    print("Solo se permiten letras.")
    jugador = input("Nombre del agente: ")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"\nEstado: Energía={energia} | Tiempo={tiempo} | Cerraduras={cerraduras_abiertas}/3 | Alarma={alarma} | Código='{codigo_parcial}'")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")
    
    opc = input("Opción: ")
    while not opc.isdigit() or int(opc) < 1 or int(opc) > 3:
        print("Ingrese una opción válida (1-3).")
        opc = input("Opción: ")
    opcion = int(opc)

    if opcion == 1:
        racha_forzar += 1
        energia -= 20
        tiempo -= 2
        
        if racha_forzar == 3:
            alarma = True
            print("Forzaste 3 veces seguidas: se trabó la cerradura y sonó la alarma.")
        else:
            if energia < 40:
                print("¡Riesgo de alarma por baja energía!")
                riesgo = input("Elige un número de seguridad (1-3): ")
                while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                    print("Debe ser un número del 1 al 3.")
                    riesgo = input("Elige un número de seguridad (1-3): ")
                if int(riesgo) == 3:
                    alarma = True
                    print("¡Se activó la alarma!")

            if not alarma:
                cerraduras_abiertas += 1
                print("¡Abriste 1 cerradura!")
            else:
                print("No pudiste abrir la cerradura porque la alarma está activa.")

    elif opcion == 2:
        racha_forzar = 0
        energia -= 10
        tiempo -= 3
        print("Hackeando panel...")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {paso}/4 - Código: {codigo_parcial}")
            
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completado! Se abrió 1 cerradura.")

    elif opcion == 3:
        racha_forzar = 0
        tiempo -= 1
        if alarma:
            energia += 5
            print("Descansaste con alarma activa (+5 energía).")
        else:
            energia += 15
            print("Descansaste (+15 energía).")
            
        if energia > 100:
            energia = 100

print("\n=== RESULTADO FINAL ===")
if cerraduras_abiertas >= 3:
    print("¡VICTORIA! Abriste todas las cerraduras.")
elif alarma and tiempo <= 3:
    print("DERROTA. El sistema se bloqueó por alarma y falta de tiempo.")
else:
    print("DERROTA. Te quedaste sin energía o sin tiempo.")

salir = input("\nMarque 0 para salir de la terminal: ")
while salir != "0":
    salir = input("Marque 0 para salir de la terminal: ")

