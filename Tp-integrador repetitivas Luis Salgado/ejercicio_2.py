# ==============================================================================
# EJERCICIO 2 — “Acceso al Campus y Menú Seguro”
# Objetivo: Login con intentos + menú de acciones con validación estricta.
# ==============================================================================

def ejercicio_2():
    print("\n--- EJERCICIO 2: ACCESO AL CAMPUS Y MENÚ SEGURO ---")
    
    # 1. Credenciales fijas
    usuario = "alumno"
    clave = "python123"
    
    intentos = 0
    ingreso = False
    
    # 2. Sistema de autenticación con máximo 3 intentos
    while intentos < 3 and not ingreso:
        intentos += 1
        print(f"\nIntento {intentos}/3")
        user = input("Usuario: ")
        passw = input("Clave: ")
        
        if user == usuario and passw == clave:
            ingreso = True
            print("Acceso concedido.")
        else:
            print("Credenciales inválidas.")
    
    # 3. Verificación de bloqueo
    if not ingreso:
        print("\nCuenta bloqueada")
        return
    
    # 4. Menú de opciones (bucle while)
    salir = False
    while not salir:
        print("\n" + "="*40)
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion_str = input("Opción: ")
        
        # 5. Validación de la opción elegida
        if not opcion_str.isdigit():
            print("Ingrese un número válido.")
            continue
        
        opcion = int(opcion_str)
        if opcion < 1 or opcion > 4:
            print("Opción fuera de rango.")
            continue
        
        # Ejecución de la opción
        if opcion == 1:
            print("\nEstado de inscripción: Inscripto")
        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")
            # Validación de longitud mínima de 6 caracteres
            if len(nueva_clave) < 6:
                print("Mínimo 6 caracteres.")
            else:
                confirmacion = input("Confirmar nueva clave: ")
                if nueva_clave == confirmacion:
                    clave = nueva_clave
                    print("Clave cambiada con éxito.")
                else:
                    print("Las contraseñas no coinciden.")
        elif opcion == 3:
            print("\nFrase motivacional: 'El éxito es la suma de pequeños esfuerzos repetidos día tras día.'")
        elif opcion == 4:
            print("\nCerrando sesión del campus...")
            salir = True

if __name__ == "__main__":
    ejercicio_2()
