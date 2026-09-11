# ==============================================================================
# EJERCICIO 1 — “Caja del Kiosco”
# Objetivo: Simular una compra con validaciones y cálculo de total.
# ==============================================================================

def ejercicio_1():
    print("\n--- EJERCICIO 1: CAJA DEL KIOSCO ---")
    
    # 1. Validación del nombre del cliente (solo letras y no vacío)
    nombre_cliente = input("Cliente: ")
    while not nombre_cliente.isalpha():
        print("Solo se permiten letras y no puede quedar vacío.")
        nombre_cliente = input("Cliente: ")
    
    # 2. Validación de la cantidad de productos (> 0 y solo dígitos)
    cantidad = input("Cantidad de productos: ")
    while not cantidad.isdigit() or int(cantidad) <= 0:
        print("Ingrese una cantidad entera positiva mayor a 0.")
        cantidad = input("Cantidad de productos: ")
    
    cantidad_productos = int(cantidad)
    
    # Acumuladores para los cálculos
    total_sin_descuento = 0
    total_con_descuento = 0.0
    
    # 3. Ciclo for por cada producto
    for i in range(1, cantidad_productos + 1):
        # Validación del precio del producto
        precio = input(f"Producto {i} - Precio: ")
        while not precio.isdigit() or int(precio) <= 0:
            print("Ingrese un precio válido (número entero positivo).")
            precio = input(f"Producto {i} - Precio: ")
        
        precio = int(precio)
        total_sin_descuento += precio
        
        # Validación de respuesta de descuento (S/N)
        desc_resp = input(f"Producto {i} - Descuento (S/N): ").lower()
        while desc_resp != "s" and desc_resp != "n":
            print("Ingrese 'S' para Sí o 'N' para No.")
            desc_resp = input(f"Producto {i} - Descuento (S/N): ").lower()
        
        # Aplicación del 10% de descuento si corresponde
        if desc_resp == "s":
            precio_final = precio * 0.90
        else:
            precio_final = float(precio)
            
        total_con_descuento += precio_final

    # 4. Cálculos finales
    ahorro_total = total_sin_descuento - total_con_descuento
    promedio_por_producto = total_con_descuento / cantidad_productos
    
    # Muestra de resultados
    print("\n--- RESUMEN DE COMPRA ---")
    print(f"Total sin descuentos: ${total_sin_descuento}")
    print(f"Total con descuentos: ${total_con_descuento:.2f}")
    print(f"Ahorro: ${ahorro_total:.2f}")
    print(f"Promedio por producto: ${promedio_por_producto:.2f}")

if __name__ == "__main__":
    ejercicio_1()
