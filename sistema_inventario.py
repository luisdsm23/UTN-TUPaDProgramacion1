# ==============================================================================
# SISTEMA DE CONTROL DE INVENTARIO - FERRETERIA
# Parcial 1 - Programacion 1 (UTN FRM)
# ==============================================================================

# 1. DECLARACION DE LISTAS PARALELAS FUERA DEL BUCLE PRINCIPAL
herramientas = []
existencias = []
ejecutando = True

# 2. BUCLE PRINCIPAL PERSISTENTE
while ejecutando:
    print('\n========================================')
    print('      SISTEMA DE CONTROL DE INVENTARIO   ')
    print('========================================')
    print('1. Carga Inicial de Herramientas')
    print('2. Carga de Existencias')
    print('3. Visualizacion de Inventario')
    print('4. Consulta de Stock')
    print('5. Reporte de Agotados')
    print('6. Alta de Nuevo Producto')
    print('7. Actualizacion de Stock (Venta/Ingreso)')
    print('8. Salir')
    print('========================================')
    
    opcion = input('Seleccione una opcion (1-8): ').strip()
    print()

    # --------------------------------------------------------------------------
    # OPCION 1: Carga Inicial de Herramientas
    # --------------------------------------------------------------------------
    if opcion == '1':
        cantidad_valida = False
        while not cantidad_valida:
            cant_str = input('Cuantas herramientas desea registrar?: ').strip()
            if cant_str.isdigit() and int(cant_str) > 0:
                cantidad = int(cant_str)
                cantidad_valida = True
            else:
                print('Error: Ingrese un numero entero mayor a 0.')

        herramientas = []
        existencias = []

        for i in range(cantidad):
            nombre_valido = False
            while not nombre_valido:
                nombre = input(f'Nombre de la herramienta #{i + 1}: ').strip()
                if nombre == '':
                    print('Error: El nombre no puede estar vacio.')
                elif nombre in herramientas:
                    print(f'Error: La herramienta "{nombre}" ya fue ingresada.')
                else:
                    herramientas.append(nombre)
                    existencias.append(0)  # Sincronia inicial en 0
                    nombre_valido = True
        print(f'Se cargaron exitosamente {cantidad} herramientas.')

    # --------------------------------------------------------------------------
    # OPCION 2: Carga de Existencias
    # --------------------------------------------------------------------------
    elif opcion == '2':
        if len(herramientas) == 0:
            print('Aviso: Primero debe realizar la carga inicial (Opcion 1).')
        else:
            print('--- Carga de Existencias por Herramienta ---')
            for i in range(len(herramientas)):
                stock_valido = False
                while not stock_valido:
                    # Requisito expreso: mostrar el nombre de la herramienta
                    stock_str = input(f'Existencias para "{herramientas[i]}": ').strip()
                    if stock_str.isdigit():
                        existencias[i] = int(stock_str)
                        stock_valido = True
                    else:
                        print('Error: Debe ser un entero mayor o igual a 0.')
            print('Existencias actualizadas correctamente.')

    # --------------------------------------------------------------------------
    # OPCION 3: Visualizacion de Inventario
    # --------------------------------------------------------------------------
    elif opcion == '3':
        if len(herramientas) == 0:
            print('El inventario esta vacio. No hay herramientas registradas.')
        else:
            print('========================================')
            print(f'{"Indice":<8} | {"Herramienta":<20} | {"Stock":<6}')
            print('----------------------------------------')
            for i in range(len(herramientas)):
                print(f'{i + 1:<8} | {herramientas[i]:<20} | {existencias[i]:<6}')
            print('========================================')

    # --------------------------------------------------------------------------
    # OPCION 4: Consulta de Stock
    # --------------------------------------------------------------------------
    elif opcion == '4':
        if len(herramientas) == 0:
            print('No hay herramientas registradas en el catalogo.')
        else:
            busqueda = input('Nombre de la herramienta a consultar: ').strip()
            if busqueda in herramientas:
                indice = herramientas.index(busqueda)
                print(f'La herramienta "{busqueda}" tiene {existencias[indice]} unidades.')
            else:
                print(f'Error: La herramienta "{busqueda}" no existe en el catalogo.')

    # --------------------------------------------------------------------------
    # OPCION 5: Reporte de Agotados
    # --------------------------------------------------------------------------
    elif opcion == '5':
        if len(herramientas) == 0:
            print('No hay herramientas registradas en el catalogo.')
        else:
            hay_agotados = False
            print('--- Herramientas Agotadas (Stock 0) ---')
            for i in range(len(existencias)):
                if existencias[i] == 0:
                    print(f'- {herramientas[i]} (0 unidades)')
                    hay_agotados = True
            if not hay_agotados:
                print('No hay productos con stock en cero actualmente.')

    # --------------------------------------------------------------------------
    # OPCION 6: Alta de Nuevo Producto
    # --------------------------------------------------------------------------
    elif opcion == '6':
        nuevo_nombre = input('Ingrese el nombre de la nueva herramienta: ').strip()
        if nuevo_nombre == '':
            print('Error: El nombre no puede estar vacio. Volviendo al menu...')
        elif nuevo_nombre in herramientas:
            print(f'Error: "{nuevo_nombre}" ya existe. Volviendo al menu...')
        else:
            stock_str = input(f'Stock inicial de "{nuevo_nombre}": ').strip()
            if not stock_str.isdigit():
                print('Error: Existencia invalida (debe ser >= 0). Volviendo al menu...')
            else:
                nuevo_stock = int(stock_str)
                herramientas.append(nuevo_nombre)
                existencias.append(nuevo_stock)
                print(f'Herramienta "{nuevo_nombre}" agregada con {nuevo_stock} unidades.')

    # --------------------------------------------------------------------------
    # OPCION 7: Actualizacion de Stock (Venta / Ingreso)
    # --------------------------------------------------------------------------
    elif opcion == '7':
        if len(herramientas) == 0:
            print('No hay herramientas registradas en el catalogo.')
        else:
            herramienta_op = input('Ingrese el nombre de la herramienta: ').strip()
            if herramienta_op not in herramientas:
                print(f'Error: La herramienta "{herramienta_op}" no existe.')
            else:
                indice = herramientas.index(herramienta_op)
                print(f'Herramienta: {herramientas[indice]} | Stock: {existencias[indice]}')
                print('a) Venta (disminuir stock)')
                print('b) Ingreso (aumentar stock por reposicion)')
                sub_opcion = input('Seleccione operacion (a/b): ').strip().lower()

                if sub_opcion == 'a':
                    unid_str = input('Cantidad a vender: ').strip()
                    if unid_str.isdigit() and int(unid_str) > 0:
                        unidades = int(unid_str)
                        if unidades <= existencias[indice]:
                            existencias[indice] -= unidades
                            print(f'Venta exitosa. Stock restante: {existencias[indice]}')
                        else:
                            print(f'Error: Stock insuficiente ({existencias[indice]} disponibles).')
                    else:
                        print('Error: Ingrese un numero entero mayor a 0.')

                elif sub_opcion == 'b':
                    unid_str = input('Cantidad a ingresar: ').strip()
                    if unid_str.isdigit() and int(unid_str) > 0:
                        unidades = int(unid_str)
                        existencias[indice] += unidades
                        print(f'Ingreso registrado. Nuevo stock: {existencias[indice]}')
                    else:
                        print('Error: Ingrese un numero entero mayor a 0.')
                else:
                    print('Error: Opcion de actualizacion invalida.')

    # --------------------------------------------------------------------------
    # OPCION 8: Salir
    # --------------------------------------------------------------------------
    elif opcion == '8':
        print('Finalizando el sistema de inventario. Hasta pronto!')
        ejecutando = False

    else:
        print('Opcion no valida. Seleccione un numero del 1 al 8.')