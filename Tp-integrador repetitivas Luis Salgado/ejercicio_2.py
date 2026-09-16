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

usuario = "alumno"
clave = "python123"
intentos = 0
ingreso = False

while intentos < 3 and not ingreso:
    intentos += 1
    print(f"Intento {intentos}/3")
    user = input("Usuario: ")
    passw = input("Clave: ")
    
    if user == usuario and passw == clave:
        ingreso = True
        print("Acceso concedido.")
    else:
        print("Credenciales inválidas.")

if not ingreso:
    print("Cuenta bloqueada")
else:
    opcion = 0
    while opcion != 4:
        print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opc_str = input("Opción: ")
        
        if not opc_str.isdigit():
            print("Ingrese un número válido.")
        elif int(opc_str) < 1 or int(opc_str) > 4:
            print("Opción fuera de rango.")
        else:
            opcion = int(opc_str)
            if opcion == 1:
                print("Inscripto")
            elif opcion == 2:
                nueva_clave = input("Nueva clave: ")
                if len(nueva_clave) < 6:
                    print("Mínimo 6 caracteres.")
                else:
                    confirmacion = input("Confirmar clave: ")
                    if nueva_clave == confirmacion:
                        clave = nueva_clave
                        print("Clave actualizada con éxito.")
                    else:
                        print("Las claves no coinciden.")
            elif opcion == 3:
                print("Frase: 'El esfuerzo de hoy es el éxito del mañana.'")
            elif opcion == 4:
                print("Sesión cerrada.")

salir = input("\nMarque 0 para salir de la terminal: ")
while salir != "0":
    salir = input("Marque 0 para salir de la terminal: ")