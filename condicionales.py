#1)Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingresa tu Edad: "))  
if edad < 0:
    print("Edad no válida no se permiten numeros negativos en la edad")
elif edad > 122:
    print("122 años es lo mas que a vivido un ser humano en el ultimo siglo, no inventes numeros!")
elif edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#Este codigo le agrege un par de validaciones teniendo en cuenta de que un usuario puede probar con numeros negaivos o demasiado altos.

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = float(input("Ingresa tu nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#este codigo te muestra si la nota es mayor o igual a 6 es aprovado, si es menor desaprobado, no agregue validaciones extra porque en base a notas solo con saber si es mas o menos de 6 tenes una respuesta si aprueba o no la persona.

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso deloperador de módulo (%) en Python para evaluar si un número es par o impar.
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#el modulo % basicamente te da los numeros que sobran en una division, por lo tanto si queda en 0 significa que el numero es par, pero si queda en 1 o algo diferente significa que es impar.


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingresa tu Edad: "))

if edad < 0:
    print("Edad no válida no se permiten numeros negativos en la edad")
elif edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#este codigo te muestra en diferentes validaciones la etapa de la edad de una persona, a este codigo no le agregue validaciones extras de las indicadas como en la primera porque preferi simplificarlo para no extederme absolutamente en todos los codigos.

#5)Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contraseña = input("Ingresa una contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#el len() es una herramiente que te permite la cantidad de caracteres que tiene un string. 

#6)escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for _ in range(100)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

if media > mediana:
    print("Sesgo positivo") 
elif media < mediana:
    print("Sesgo negativo")
else:
    print("No hay sesgo")

#aca se importaron 2 librerias, ramdom y statics. con ramdom se uso para generar numeros aleatorios, y con statistics se uso para calcular la moda, mediana y media.

#7)Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase = input("Ingresa una frase o palabra: ")

if frase[-1].lower() in 'aeiou':
    frase += '!'
print(frase)
#si la frase termina en una vocal le pone un "!" sino no pone nada

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingresa tu nombre: ")
opcion = int(input("Selecciona una opción (1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula): "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

#el upper convierte en mayusculas, el lower en minusculas y el title convierte la primera letra en mayusculas.

#9)  Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

terremoto = float(input("Ingresa la magnitud del terremoto: "))
if terremoto < 3:
    print("Muy leve (imperceptible)")
elif terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#float porque los terremotos tienen decimales normalmente. Y use una estructura basica en base a varias validaciones.

#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("¿Qué mes del año es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia < 20):
        print("Estás en invierno")
    elif (mes == 3 and dia >= 20) or (mes <= 6 and dia < 21):
        print("Estás en primavera")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia < 22):
        print("Estás en verano")
    else:
        print("Estás en otoño")

elif hemisferio == 'S':
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia < 20):
        print("Estás en verano")
    elif (mes == 3 and dia >= 20) or (mes <= 6 and dia < 21):
        print("Estás en otoño")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia < 22):
        print("Estás en invierno")
    else:
        print("Estás en primavera")
else:
    print("Hemisferio no válido. Por favor, ingresa 'N' o 'S'.")

#saque las fechas de cada estacion de wikipediaS, y con base a eso hice las validaciones para cada estacion dependiendo del hemisferio.