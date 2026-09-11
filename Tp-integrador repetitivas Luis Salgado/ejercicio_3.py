# ==============================================================================
# EJERCICIO 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
# Contexto: 2 días de atención (Lunes: 4 turnos, Martes: 3 turnos).
# Restricciones:
# - NO listas, NO diccionarios, NO sets, NO tuplas.
# - Variables individuales para cada turno ("", libre).
# - Validaciones con .isalpha() y .isdigit() sin try/except.
# ==============================================================================

def ejercicio_3():
    print("\n--- EJERCICIO 3: AGENDA DE TURNOS CON NOMBRES (SIN LISTAS) ---")
    
    # Variables individuales para los turnos (cadena vacía "" representa turno libre)
    lunes1 = ""
    lunes2 = ""
    lunes3 = ""
    lunes4 = ""
    
    martes1 = ""
    martes2 = ""
    martes3 = ""
    
    # 1. Pedir y validar nombre del operador
    operador = input("Nombre del operador: ")
    while not operador.isalpha():
        print("Solo se permiten letras.")
        operador = input("Nombre del operador: ")
    
    print(f"\nBienvenido/a, operador/a {operador}.")
    
    # 2. Menú principal
    cerrar_sistema = False
    while not cerrar_sistema:
        print("\n" + "="*45)
        print("--- MENÚ DE TURNOS ---")
        print("1. Reservar turno")
        print("2. Cancelar turno (por nombre)")
        print("3. Ver agenda del día")
        print("4. Ver resumen general")
        print("5. Cerrar sistema")
        
        opc_str = input("Opción: ")
        while not opc_str.isdigit() or int(opc_str) < 1 or int(opc_str) > 5:
            print("Ingrese una opción numérica válida (1 al 5).")
            opc_str = input("Opción: ")
        
        opcion = int(opc_str)
        
        # --- OPCIÓN 1: RESERVAR TURNO ---
        if opcion == 1:
            print("\n--- Reservar Turno ---")
            dia_str = input("Elija día (1=Lunes, 2=Martes): ")
            while dia_str != "1" and dia_str != "2":
                print("Opción de día inválida. Debe ser 1 o 2.")
                dia_str = input("Elija día (1=Lunes, 2=Martes): ")
            
            nombre_paciente = input("Nombre del paciente: ")
            while not nombre_paciente.isalpha():
                print("Solo se permiten letras.")
                nombre_paciente = input("Nombre del paciente: ")
            
            nombre_paciente_limpio = nombre_paciente.capitalize()
            
            if dia_str == "1":
                # Validar que no esté repetido el lunes
                if (nombre_paciente_limpio == lunes1 or 
                    nombre_paciente_limpio == lunes2 or 
                    nombre_paciente_limpio == lunes3 or 
                    nombre_paciente_limpio == lunes4):
                    print(f"El paciente '{nombre_paciente_limpio}' ya tiene un turno reservado el Lunes.")
                # Asignar en el primer espacio libre
                elif lunes1 == "":
                    lunes1 = nombre_paciente_limpio
                    print(f"Turno 1 del Lunes asignado a {nombre_paciente_limpio}.")
                elif lunes2 == "":
                    lunes2 = nombre_paciente_limpio
                    print(f"Turno 2 del Lunes asignado a {nombre_paciente_limpio}.")
                elif lunes3 == "":
                    lunes3 = nombre_paciente_limpio
                    print(f"Turno 3 del Lunes asignado a {nombre_paciente_limpio}.")
                elif lunes4 == "":
                    lunes4 = nombre_paciente_limpio
                    print(f"Turno 4 del Lunes asignado a {nombre_paciente_limpio}.")
                else:
                    print("No hay cupos disponibles para el día Lunes.")
                    
            elif dia_str == "2":
                # Validar que no esté repetido el martes
                if (nombre_paciente_limpio == martes1 or 
                    nombre_paciente_limpio == martes2 or 
                    nombre_paciente_limpio == martes3):
                    print(f"El paciente '{nombre_paciente_limpio}' ya tiene un turno reservado el Martes.")
                # Asignar en el primer espacio libre
                elif martes1 == "":
                    martes1 = nombre_paciente_limpio
                    print(f"Turno 1 del Martes asignado a {nombre_paciente_limpio}.")
                elif martes2 == "":
                    martes2 = nombre_paciente_limpio
                    print(f"Turno 2 del Martes asignado a {nombre_paciente_limpio}.")
                elif martes3 == "":
                    martes3 = nombre_paciente_limpio
                    print(f"Turno 3 del Martes asignado a {nombre_paciente_limpio}.")
                else:
                    print("No hay cupos disponibles para el día Martes.")

        # --- OPCIÓN 2: CANCELAR TURNO ---
        elif opcion == 2:
            print("\n--- Cancelar Turno ---")
            dia_str = input("Elija día (1=Lunes, 2=Martes): ")
            while dia_str != "1" and dia_str != "2":
                print("Opción de día inválida. Debe ser 1 o 2.")
                dia_str = input("Elija día (1=Lunes, 2=Martes): ")
            
            nombre_paciente = input("Nombre del paciente a cancelar: ")
            while not nombre_paciente.isalpha():
                print("Solo se permiten letras.")
                nombre_paciente = input("Nombre del paciente a cancelar: ")
            
            nombre_paciente_limpio = nombre_paciente.capitalize()
            cancelado = False
            
            if dia_str == "1":
                if lunes1 == nombre_paciente_limpio:
                    lunes1 = ""
                    cancelado = True
                elif lunes2 == nombre_paciente_limpio:
                    lunes2 = ""
                    cancelado = True
                elif lunes3 == nombre_paciente_limpio:
                    lunes3 = ""
                    cancelado = True
                elif lunes4 == nombre_paciente_limpio:
                    lunes4 = ""
                    cancelado = True
            elif dia_str == "2":
                if martes1 == nombre_paciente_limpio:
                    martes1 = ""
                    cancelado = True
                elif martes2 == nombre_paciente_limpio:
                    martes2 = ""
                    cancelado = True
                elif martes3 == nombre_paciente_limpio:
                    martes3 = ""
                    cancelado = True
                    
            if cancelado:
                print(f"Turno del paciente '{nombre_paciente_limpio}' cancelado correctamente.")
            else:
                print(f"No se encontró ningún turno para el paciente '{nombre_paciente_limpio}' en ese día.")

        # --- OPCIÓN 3: VER AGENDA DEL DÍA ---
        elif opcion == 3:
            print("\n--- Ver Agenda del Día ---")
            dia_str = input("Elija día (1=Lunes, 2=Martes): ")
            while dia_str != "1" and dia_str != "2":
                print("Opción de día inválida. Debe ser 1 o 2.")
                dia_str = input("Elija día (1=Lunes, 2=Martes): ")
            
            if dia_str == "1":
                print("\nAgenda del LUNES:")
                print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
            else:
                print("\nAgenda del MARTES:")
                print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

        # --- OPCIÓN 4: VER RESUMEN GENERAL ---
        elif opcion == 4:
            # Conteo de ocupados de Lunes
            ocupados_lunes = 0
            if lunes1 != "":
                ocupados_lunes += 1
            if lunes2 != "":
                ocupados_lunes += 1
            if lunes3 != "":
                ocupados_lunes += 1
            if lunes4 != "":
                ocupados_lunes += 1
            disponibles_lunes = 4 - ocupados_lunes
            
            # Conteo de ocupados de Martes
            ocupados_martes = 0
            if martes1 != "":
                ocupados_martes += 1
            if martes2 != "":
                ocupados_martes += 1
            if martes3 != "":
                ocupados_martes += 1
            disponibles_martes = 3 - ocupados_martes
            
            print("\n--- RESUMEN GENERAL ---")
            print(f"Lunes: {ocupados_lunes} turnos ocupados | {disponibles_lunes} turnos disponibles")
            print(f"Martes: {ocupados_martes} turnos ocupados | {disponibles_martes} turnos disponibles")
            
            if ocupados_lunes > ocupados_martes:
                print("Día con más turnos ocupados: Lunes")
            elif ocupados_martes > ocupados_lunes:
                print("Día con más turnos ocupados: Martes")
            else:
                print("Empate: Ambos días tienen la misma cantidad de turnos ocupados.")

        # --- OPCIÓN 5: CERRAR SISTEMA ---
        elif opcion == 5:
            print("\nCerrando sistema de turnos. ¡Hasta luego!")
            cerrar_sistema = True

if __name__ == "__main__":
    ejercicio_3()
