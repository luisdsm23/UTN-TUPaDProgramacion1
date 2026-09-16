#3) Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
#Contexto: Hay 2 días de atención: Lunes y Martes. Cada día tiene cupos fijos: Lunes: 4 turnos, Martes: 3 turnos.
#Reglas:
#1. Pedir nombre del operador (solo letras).
#2. Menú repetitivo hasta salir:
#   1. Reservar turno
#   2. Cancelar turno (por nombre)
#   3. Ver agenda del día
#   4. Ver resumen general
#   5. Cerrar sistema
#3. Reservar: Elegir día (1=Lunes, 2=Martes). Pedir nombre del paciente (solo letras). Verificar que no esté repetido en ese día. Guardar en el primer espacio libre (ej. lunes1, lunes2…).
#4. Cancelar: Elegir día. Pedir nombre del paciente (solo letras). Si existe, cancelar y dejar el espacio vacío ("").
#5. Ver agenda del día: Mostrar turnos del día en orden (Turno 1..N), indicando “(libre)” si está vacío.
#6. Resumen general: Turnos ocupados y disponibles por día. Día con más turnos (o empate).
#Restricciones: No listas, no diccionarios, no sets, no tuplas. Se permite usar "" como vacío. Validaciones con .isalpha() y .isdigit() (sin try/except).

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Solo se permiten letras.")
    operador = input("Nombre del operador: ")

opcion_menu = 0
while opcion_menu != 5:
    print("\n1. Reservar turno")
    print("2. Cancelar turno (por nombre)")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opc = input("Opción: ")
    while not opc.isdigit() or int(opc) < 1 or int(opc) > 5:
        print("Ingrese una opción entre 1 y 5.")
        opc = input("Opción: ")
    opcion_menu = int(opc)

    if opcion_menu == 1:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Opción inválida. Ingrese 1 o 2.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            
        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            print("Solo se permiten letras.")
            paciente = input("Nombre del paciente: ")

        if dia == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("El paciente ya tiene turno el día Lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print(f"Turno 1 asignado a {paciente}")
            elif lunes2 == "":
                lunes2 = paciente
                print(f"Turno 2 asignado a {paciente}")
            elif lunes3 == "":
                lunes3 = paciente
                print(f"Turno 3 asignado a {paciente}")
            elif lunes4 == "":
                lunes4 = paciente
                print(f"Turno 4 asignado a {paciente}")
            else:
                print("No hay cupos disponibles el día Lunes.")
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("El paciente ya tiene turno el día Martes.")
            elif martes1 == "":
                martes1 = paciente
                print(f"Turno 1 asignado a {paciente}")
            elif martes2 == "":
                martes2 = paciente
                print(f"Turno 2 asignado a {paciente}")
            elif martes3 == "":
                martes3 = paciente
                print(f"Turno 3 asignado a {paciente}")
            else:
                print("No hay cupos disponibles el día Martes.")

    elif opcion_menu == 2:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Opción inválida. Ingrese 1 o 2.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            
        paciente = input("Nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            print("Solo se permiten letras.")
            paciente = input("Nombre del paciente a cancelar: ")

        cancelado = False
        if dia == "1":
            if lunes1 == paciente:
                lunes1 = ""
                cancelado = True
            elif lunes2 == paciente:
                lunes2 = ""
                cancelado = True
            elif lunes3 == paciente:
                lunes3 = ""
                cancelado = True
            elif lunes4 == paciente:
                lunes4 = ""
                cancelado = True
        else:
            if martes1 == paciente:
                martes1 = ""
                cancelado = True
            elif martes2 == paciente:
                martes2 = ""
                cancelado = True
            elif martes3 == paciente:
                martes3 = ""
                cancelado = True

        if cancelado:
            print("Turno cancelado exitosamente.")
        else:
            print("No se encontró al paciente en la agenda de ese día.")

    elif opcion_menu == 3:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Opción inválida. Ingrese 1 o 2.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            
        if dia == "1":
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    elif opcion_menu == 4:
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1
        libres_lunes = 4 - ocupados_lunes

        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1
        libres_martes = 3 - ocupados_martes

        print(f"Lunes - Ocupados: {ocupados_lunes}, Disponibles: {libres_lunes}")
        print(f"Martes - Ocupados: {ocupados_martes}, Disponibles: {libres_martes}")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate en cantidad de turnos")

    elif opcion_menu == 5:
        print("Cerrando sistema...")

salir = input("\nMarque 0 para salir de la terminal: ")
while salir != "0":
    salir = input("Marque 0 para salir de la terminal: ")

