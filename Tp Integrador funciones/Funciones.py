lista_paises=[{"nombre":"Argentina",
               "poblacion":46466688,
               "superficie":2780400, 
               "continente":"america"},
               {"nombre":"Brasil",
               "poblacion":213562666,
               "superficie":8515770 , 
               "continente":"america"},
               {"nombre":"Venezuela",
               "poblacion":1075987,
               "superficie":916445, 
               "continente":"america"},
               {"nombre":"Chile",
               "poblacion":20150948,
               "superficie":2006354, 
               "continente":"america"},
               {"nombre":"Uruguay",
               "poblacion":3499451,
               "superficie":176215, 
               "continente":"america"},
               {"nombre":"Colombia",
               "poblacion":2070408,
               "superficie":1141748, 
               "continente":"america"}]


def agregar_pais():
    nombre = input("Nombre del pais: ").strip()
    while not nombre:
        print("El nombre no puede estar vacio.")
        nombre = input("Nombre del pais: ").strip()

    poblacion = None
    while poblacion is None:
        try:
            poblacion = int(input("Poblacion: "))
            if poblacion <= 0:
                print("La poblacion debe ser mayor que cero.")
                poblacion = None
        except ValueError:
            print("Ingresa un numero entero valido para la poblacion.")

    superficie = None
    while superficie is None:
        try:
            superficie = int(input("Superficie en km2: "))
            if superficie <= 0:
                print("La superficie debe ser mayor que cero.")
                superficie = None
        except ValueError:
            print("Ingresa un numero valido para la superficie.")

    continente = input("Continente: ").strip()
    while not continente:
        print("El continente no puede estar vacio.")
        continente = input("Continente: ").strip()

    lista_paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    })
    print("Pais agregado correctamente.")


