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
    print("Solo se permiten letras y no puede quedar vacío.")
    nombre_cliente = input("Cliente: ")

cantidad = input("Cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Ingrese una cantidad válida mayor a 0.")
    cantidad = input("Cantidad de productos: ")
cantidad = int(cantidad)

total_sin_descuentos = 0
total_con_descuentos = 0.0

for i in range(1, cantidad + 1):
    precio = input(f"Producto {i} - Precio: ")
    while not precio.isdigit() or int(precio) <= 0:
        print("Ingrese un precio numérico válido.")
        precio = input(f"Producto {i} - Precio: ")
    precio = int(precio)
    
    total_sin_descuentos += precio

    descuento = input(f"Producto {i} - Descuento (S/N): ").lower()
    while descuento != "s" and descuento != "n":
        print("Ingrese 's' para Sí o 'n' para No.")
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

salir = input("\nMarque 0 para salir de la terminal: ")
while salir != "0":
    salir = input("Marque 0 para salir de la terminal: ")


