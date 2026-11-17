# Ejercicio 1.1
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# Ejercicio 1.2
def mayor_de_tres(a, b, c):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor


# Ejercicio 1.3
def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return round(promedio, 2)


# Ejercicio 1.4
def clasificar_nota(nota):
    if nota < 0 or nota > 10:
        return "Nota inválida"
    elif nota < 6:
        return "Desaprobado"
    elif nota < 8:
        return "Aprobado"
    else:
        return "Promocionado"


# Ejercicio 1.5
def aplicar_descuento(precio, porcentaje):
    if porcentaje < 0 or porcentaje > 100:
        return precio
    descuento = precio * (porcentaje / 100)
    return precio - descuento


# Ejercicio 2.1
def sumar_lista(numeros):
    total = 0
    for num in numeros:
        total = total + num
    return total


# Ejercicio 2.2
def contar_mayores(numeros, limite):
    cantidad = 0
    for num in numeros:
        if num > limite:
            cantidad = cantidad + 1
    return cantidad


# Ejercicio 2.3
def filtrar_pares(numeros):
    pares = []
    for num in numeros:
        if es_par(num):
            pares.append(num)
    return pares


# Ejercicio 2.4
def buscar_posicion(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1


# Ejercicio 2.5
def invertir_lista(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida


# Ejercicio 2.6
def promedio_lista(numeros):
    if len(numeros) == 0:
        return 0
    total = sumar_lista(numeros)
    promedio = total / len(numeros)
    return round(promedio, 2)


# Ejercicio 3.1
def minimo_y_maximo(numeros):
    minimo = numeros[0]
    maximo = numeros[0]
    for num in numeros:
        if num < minimo:
            minimo = num
        if num > maximo:
            maximo = num
    return (minimo, maximo)


# Ejercicio 3.2
def distancia(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(dist, 2)


# Ejercicio 3.3
def mejor_alumno(alumnos):
    mejor = alumnos[0]
    for alumno in alumnos:
        if alumno[1] > mejor[1]:
            mejor = alumno
    return mejor


# Ejercicio 3.4
def nombres_aprobados(alumnos, nota_minima):
    aprobados = []
    for nombre, nota in alumnos:
        if nota >= nota_minima:
            aprobados.append(nombre)
    return aprobados


# Ejercicio 3.5
# Las tuplas son inmutables, no se pueden modificar sus valores una vez creadas
def actualizar_nota(alumnos, nombre, nueva_nota):
    nueva_lista = []
    for al_nombre, al_nota in alumnos:
        if al_nombre == nombre:
            nueva_lista.append((al_nombre, nueva_nota))
        else:
            nueva_lista.append((al_nombre, al_nota))
    return nueva_lista


# Ejercicio 4.1
def eliminar_repetidos(lista):
    return set(lista)


# Ejercicio 4.2
def letras_distintas(palabra):
    letras = set()
    palabra_minuscula = palabra.lower()
    for letra in palabra_minuscula:
        letras.add(letra)
    return len(letras)


# Ejercicio 4.3
def en_ambas(curso1, curso2):
    return curso1 & curso2


# Ejercicio 4.4
def solo_en_una(curso1, curso2):
    return curso1 ^ curso2


# Ejercicio 4.5
def ausentes(inscriptos, presentes):
    set_inscriptos = set(inscriptos)
    set_presentes = set(presentes)
    return set_inscriptos - set_presentes


# Ejercicio 5.1
def contar_apariciones(lista):
    conteo = {}
    for elemento in lista:
        conteo[elemento] = conteo.get(elemento, 0) + 1
    return conteo


# Ejercicio 5.2
def contar_palabras(texto):
    palabras = texto.lower().split()
    return contar_apariciones(palabras)


# Ejercicio 5.3
def agregar_contacto(agenda, nombre, telefono):
    if nombre in agenda:
        return False
    agenda[nombre] = telefono
    return True


# Ejercicio 5.4
def buscar_telefono(agenda, nombre):
    return agenda.get(nombre)


# Ejercicio 5.5
def invertir_diccionario(diccionario):
    invertido = {}
    for clave, valor in diccionario.items():
        invertido[valor] = clave
    return invertido


# Ejercicio 5.6
def agrupar_por_inicial(palabras):
    grupos = {}
    for palabra in palabras:
        inicial = palabra[0].upper()
        if inicial not in grupos:
            grupos[inicial] = []
        grupos[inicial].append(palabra)
    return grupos


# Ejercicio 6
REGISTROS = [
    ("Ana", "Programación", 9),
    ("Ana", "Matemática", 7),
    ("Luis", "Programación", 5),
    ("Luis", "Inglés", 6),
    ("Sol", "Matemática", 8),
    ("Sol", "Programación", 10),
]


# Ejercicio 6.1
def obtener_materias(registros):
    materias = set()
    for registro in registros:
        materia = registro[1]
        materias.add(materia)
    return materias


# Ejercicio 6.2
def notas_por_alumno(registros):
    notas = {}
    for registro in registros:
        alumno = registro[0]
        nota = registro[2]
        if alumno not in notas:
            notas[alumno] = []
        notas[alumno].append(nota)
    return notas


# Ejercicio 6.3
def promedios_por_alumno(registros):
    notas = notas_por_alumno(registros)
    promedios = {}
    for alumno in notas:
        promedios[alumno] = promedio_lista(notas[alumno])
    return promedios


# Ejercicio 6.4
def alumnos_destacados(registros, minimo):
    promedios = promedios_por_alumno(registros)
    destacados = set()
    for alumno in promedios:
        if promedios[alumno] >= minimo:
            destacados.add(alumno)
    return destacados


# Ejercicio 6.5
def mostrar_boletin(registros):
    materias = sorted(obtener_materias(registros))
    print("Materias evaluadas:", ", ".join(materias))
    
    promedios = promedios_por_alumno(registros)
    for alumno in promedios:
        prom = promedios[alumno]
        condicion = clasificar_nota(prom)
        print(f"{alumno:<10}{prom:.2f}  {condicion}")


if __name__ == "__main__":
    print(es_par(4))
    print(mayor_de_tres(3, 9, 5))
