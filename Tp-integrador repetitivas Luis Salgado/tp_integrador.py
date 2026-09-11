#1) Ejercicio 1 — “Caja del Kiosco”
#Objetivo: Simular una compra con validaciones y cálculo de total.
#Requisitos:
#1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
#2. Pedir cantidad de productos a comprar (número entero positivo, validar con .isdigit() en while).
#3. Por cada producto (usar for):
#   o Pedir precio (entero, validar .isdigit()).
#   o Pedir si tiene descuento S/N (validar con while, aceptar s o n en cualquier mayuscula/minuscula).
#   o Si tiene descuento: aplicar 10% al precio de ese producto.
#4. Al final mostrar:
#   o Total sin descuentos
#   o Total con descuentos
#   o Ahorro total
#   o Promedio por producto (usar float y formatear con :.2f, ejem: print(f"{x:.2f}"))
#Validaciones obligatorias:
#• Sin try/except.
#• No aceptar vacío en nombre (si queda vacío, es error).
#• Cantidad > 0 (si ingresa 0, volver a pedir).

nombre_cliente = input("Cliente: ")
while not nombre_cliente.isalpha():
    print("Error: Solo se permiten letras y no puede quedar vacío.")
    nombre_cliente = input("Cliente: ")

cantidad = input("Cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: Ingrese una cantidad válida mayor a 0.")
    cantidad = input("Cantidad de productos: ")
cantidad = int(cantidad)

total_sin_descuentos = 0
total_con_descuentos = 0.0

for i in range(1, cantidad + 1):
    precio = input(f"Producto {i} - Precio: ")
    while not precio.isdigit() or int(precio) <= 0:
        print("Error: Ingrese un precio numérico válido.")
        precio = input(f"Producto {i} - Precio: ")
    precio = int(precio)
    
    total_sin_descuentos += precio

    descuento = input(f"Producto {i} - Descuento (S/N): ").lower()
    while descuento != "s" and descuento != "n":
        print("Error: Ingrese 's' para Sí o 'n' para No.")
        descuento = input(f"Producto {i} - Descuento (S/N): ").lower()

    if descuento == "s":
        total_con_descuentos += precio * 0.90
    else:
        total_con_descuentos += float(precio)

ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

print(f"\nTotal sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#En este ejercicio use .isalpha() en un while para asegurar que el nombre solo tenga letras (y no quede vacio). Con .isdigit() valide que la cantidad y los precios sean numeros positivos. Use un for con range() para repetir la carga de cada producto, acumulando el total general y aplicando el 10% de descuento (multiplicando por 0.90) si el usuario ingresaba 's'. Finalmente calcule el ahorro restando los totales y el promedio dividiendo el total por la cantidad, usando :.2f para formatear los decimales a 2 dígitos como pide la consigna.


#2) Ejercicio 2 — “Acceso al Campus y Menú Seguro”
#Objetivo: Login con intentos + menú de acciones con validación estricta.
#Requisitos:
#1. Definir credenciales fijas en el código: usuario correcto: "alumno", clave correcta: "python123"
#2. Permitir máximo 3 intentos para ingresar usuario y clave.
#3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
#4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
#   1. Ver estado de inscripción (mostrar “Inscripto”)
#   2. Cambiar clave (pedir nueva clave y confirmación; deben coincidir)
#   3. Mostrar mensaje motivacional (1 frase)
#   4. Salir
#5. Validación del menú: Debe ser número (.isdigit()) y estar entre 1 y 4
#Cambio de clave: La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, rechazar.

usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
ingreso_exitoso = False

while intentos < 3 and not ingreso_exitoso:
    intentos += 1
    print(f"Intento {intentos}/3")
    user = input("Usuario: ")
    passw = input("Clave: ")
    
    if user == usuario_correcto and passw == clave_correcta:
        ingreso_exitoso = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")

if not ingreso_exitoso:
    print("Cuenta bloqueada")
else:
    opcion = 0
    while opcion != 4:
        print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opc_str = input("Opción: ")
        
        if not opc_str.isdigit():
            print("Error: ingrese un número válido.")
        elif int(opc_str) < 1 or int(opc_str) > 4:
            print("Error: opción fuera de rango.")
        else:
            opcion = int(opc_str)
            if opcion == 1:
                print("Inscripto")
            elif opcion == 2:
                nueva_clave = input("Nueva clave: ")
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                else:
                    confirmacion = input("Confirmar clave: ")
                    if nueva_clave == confirmacion:
                        clave_correcta = nueva_clave
                        print("Clave actualizada con éxito.")
                    else:
                        print("Error: las claves no coinciden.")
            elif opcion == 3:
                print("Frase: 'El esfuerzo de hoy es el éxito del mañana.'")
            elif opcion == 4:
                print("Sesión cerrada.")

#Aca utilice un ciclo while para controlar los 3 intentos de login mediante un contador. Si acierta el usuario y contraseña pasa a un segundo while que mantiene abierto el menú hasta que se elija la opcion 4 (Salir). Con .isdigit() comprobe que la opcion sea numerica y valide que este en el rango del 1 al 4 con condicionales if/elif. Para el cambio de clave use len() para chequear que tenga 6 o mas caracteres y compare con un if que ambas claves ingresadas sean iguales.


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
    print("Error: Solo se permiten letras.")
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
        print("Error: Ingrese una opción entre 1 y 5.")
        opc = input("Opción: ")
    opcion_menu = int(opc)

    if opcion_menu == 1:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Error: Opción inválida. Ingrese 1 o 2.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            
        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            print("Error: Solo se permiten letras.")
            paciente = input("Nombre del paciente: ")

        if dia == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: El paciente ya tiene turno el día Lunes.")
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
                print("Error: El paciente ya tiene turno el día Martes.")
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
            print("Error: Opción inválida. Ingrese 1 o 2.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            
        paciente = input("Nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            print("Error: Solo se permiten letras.")
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
            print("Error: Opción inválida. Ingrese 1 o 2.")
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

#En este ejercicio, como no se pueden usar listas ni diccionarios, cree 7 variables de texto individuales (lunes1 a lunes4 y martes1 a martes3) iniciando con cadena vacia "" para representar los lugares libres. Al reservar turno primero use un if con 'or' para comprobar que el paciente no estuviera ya anotado, y luego elif encadenados para guardar el nombre en el primer turno vacio. Para cancelar se iguala la variable encontrada a "" y para el resumen conte los turnos que no estuvieran vacios usando incrementos con if.


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

nombre_agente = input("Nombre del agente: ")
while not nombre_agente.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_agente = input("Nombre del agente: ")

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
        print("Error: Ingrese una opción válida (1-3).")
        opc = input("Opción: ")
    opcion = int(opc)

    if opcion == 1:
        racha_forzar += 1
        energia -= 20
        tiempo -= 2
        
        if racha_forzar == 3:
            alarma = True
            print("¡Anti-spam! Forzaste 3 veces seguidas: se trabó la cerradura y sonó la alarma.")
        else:
            if energia < 40:
                print("¡Riesgo de alarma por baja energía!")
                riesgo = input("Elige un número de seguridad (1-3): ")
                while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                    print("Error: Debe ser un número del 1 al 3.")
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

#En este juego use variables de estado para la energia, tiempo, cerraduras y una variable booleana para la alarma. Para la regla anti-spam use un contador racha_forzar que suma 1 si forzas, y se reinicia a 0 si descansas o hackeas. En el hackeo use un for de 4 pasos para ir concatenando la letra 'A' a codigo_parcial y len() para verificar si llego a 8 caracteres y abrir la cerradura. El bucle while controla que el juego siga mientras tengas recursos y no ocurra el bloqueo por alarma.


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

print("--- BIENVENIDO A LA ARENA ---")
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
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
        print("Error: Ingrese un número válido.")
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

#Aca use variables con los tipos de datos pedidos (str, int, float y bool). La batalla corre en un ciclo while mientras ambos esten vivos (> 0 de vida). Para el ataque pesado use una condicion que evalua si la vida del enemigo es menor a 20 para aplicar el daño critico multiplicado por 1.5 en float. Para la rafaga veloz implemente un for con range(3) que resta 5 de daño por cada repeticion. La curacion chequea si quedan pociones antes de sumar 30 de vida, y tras la accion del jugador, si el enemigo sigue con vida, contraataca automaticamente.
