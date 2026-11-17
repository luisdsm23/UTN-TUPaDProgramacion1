especialidades = []
cupos = []

opcion = ""

while opcion != "8":
    print("\n--- MENÚ DE GESTION DE TURNOS ---")
    print("1. Ingesar lista de especialidades")
    print("2. Ingresar lista de cupos disponibles por especialidad")
    print("3. Mostrar agenda")
    print("4. Consultar cupos de una especialidad")
    print("5. Listar especialidades sin cupo")
    print("6. Agregar especialidad")
    print("7. Actualizar cupos (reservar / cancelar)")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
      especialidades.clear()
      cupos.clear()
      print("\n --- Ingreso de especialidades ---")

      cant = input("Ingrese la cantidad de especialidades: ").strip()
      if cant.isdigit () and int(cant) > 0:
          cant = int(cant)
          i = 0
          while i < cant:
             nombre = input(f"Ingrese el nombre de la especialidad {i + 1}: ").strip().capitalize()
             if nombre == "":
                    print("El nombre de la especialidad no puede estar vacío.")
             elif nombre in especialidades:
                    print("La especialidad ya existe. Ingrese otra.")
             else:
                    especialidades.append(nombre)
                    cupos.append(0)
             i += 1
          print("Lista de especialidades ingresadas correctamente.")
      else:
          print("Cantidad inválida. Debe ser un número entero positivo.")

    elif opcion == "2":
         if len (especialidades) == 0:
             print("\nPrimero debe ingresar especialidades (Opción 1).")

         else: 
            print("\n --- CARGAR CUPOS DISPONIBLES ---")
            i = 0
            while i < len(especialidades):
                cant_cupos = input(f"Ingrese la cantidad de cupos disponibles para {especialidades[i]}: ").strip()
                if cant_cupos.isdigit() and int(cant_cupos) >= 0:
                    cupos[i] = int(cant_cupos)
                    i += 1
                else:
                    print("Por favor, ingrese un número entero mayor o igual a 0.")
            print("Cupos cargados correctamente.")

    elif opcion == "3":
        print("\n--- AGENDA DE ESPECIALIDADES ---")
        if len(especialidades) == 0:
            print("No hay especialidades registradas.")
        else:
            i = 0
            while i < len(especialidades):
                print(f"- {especialidades[i]}: {cupos[i]} cupo(s) disponible(s)")
                i += 1

    elif opcion == "4":
        if len(especialidades) == 0:
            print("\nNo hay especialidades registradas.")
        else:
            buscar = input("\nIngrese el nombre de la especialidad a consultar: ").strip().capitalize()
            if buscar in especialidades:
                idx = especialidades.index(buscar)
                print(f"La especialidad {especialidades[idx]} tiene {cupos[idx]} cupo(s) disponible(s).")
            else:
                print("Especialidad inexistente.")

    elif opcion == "5":
        print("\n--- ESPECIALIDADES SIN CUPO ---")
        if len(especialidades) == 0:
            print("No hay especialidades registradas.")
        else:
            encontradas = False
            i = 0
            while i < len(especialidades):
                if cupos[i] == 0:
                    print(f"- {especialidades[i]}")
                    encontradas = True
                i += 1
            if not encontradas:
                print("Todas las especialidades cuentan con cupos disponibles.")

    elif opcion == "6":
        print("\n--- AGREGAR NUEVA ESPECIALIDAD ---")
        nombre = input("Nombre de la nueva especialidad: ").strip().capitalize()
        if nombre == "":
            print("El nombre no puede estar vacío.")
        elif nombre in especialidades:
            print("Esa especialidad ya existe.")
        else:
            cant_cupos = input(f"Cupos iniciales para {nombre}: ").strip()
            if cant_cupos.isdigit() and int(cant_cupos) >= 0:
                especialidades.append(nombre)
                cupos.append(int(cant_cupos))
                print(f"Especialidad {nombre} agregada con éxito.")
            else:
                print("Cantidad de cupos inválida. Debe ser un entero ≥ 0.")

    elif opcion == "7":
        if len(especialidades) == 0:
            print("\nNo hay especialidades registradas.")
        else:
            print("\n--- ACTUALIZAR CUPOS ---")
            buscar = input("Ingrese la especialidad: ").strip().capitalize()
            if buscar in especialidades:
                idx = especialidades.index(buscar)
                print(f"Especialidad seleccionada: {especialidades[idx]} (Cupos actuales: {cupos[idx]})")
                print("1. Reservar turno (disminuye cupo)")
                print("2. Cancelar turno (aumenta cupo)")
                sub_opcion = input("Elija una acción (1 o 2): ").strip()
                
                if sub_opcion == "1":
                    if cupos[idx] > 0:
                        cupos[idx] -= 1
                        print(f"Turno reservado. Cupos restantes para {especialidades[idx]}: {cupos[idx]}")
                    else:
                        print("No se puede reservar: la especialidad no tiene cupos disponibles.")
                elif sub_opcion == "2":
                    cupos[idx] += 1
                    print(f"Turno cancelado. Cupos actualizados para {especialidades[idx]}: {cupos[idx]}")
                else:
                    print("Acción no válida.")
            else:
                print("Especialidad inexistente.")

    elif opcion == "8":
        print("\nSaliendo del sistema. ¡Hasta luego!")

    else:
        print("\nOpción inválida. Por favor seleccione un número del 1 al 8.")
