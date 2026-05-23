# Aquí estoy creando una función para evitar repetir la validación de
# si es un entero o algo más

def input_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        
        except ValueError:
            print("Error: Ingresa un número entero.")

opt = 1

while opt != 2:
    print("\n==========Ley de gravitación universal==========\n")

    print("1) Sol         2) Mercurio\n"
          "3) Venus       4) Tierra\n" \
          "5) Marte       6) Jupiter\n" \
          "7) Saturno     8) Urano\n")


# Este diccionaro contendrá el peso de los objetos en kilogramos:

    cuerpos = {1: 1.989 * 10**30,           #Sol
               2: 3.30 * 10**23,            #Mercurio
               3: 4.87 * 10**24,            #Venus
               4: 5.97 * 10**24,            #Tierra
               5: 6.42 * 10**23,            #Marte
               6: 1.90 * 10**27,            #Jupiter
               7: 5.68 * 10**26,            #Saturno
               8: 8.68 * 10**25             #Urano
               }           

# Se usará la distancia de cada planeta al sol
# para aproximar la distancia entre cada objeto

    distancia= {1: 0.0,           # Sol
                2: 57.9e9,        # Mercurio
                3: 108.2e9,       # Venus
                4: 149.6e9,       # Etc...
                5: 227.9e9,
                6: 778.5e9,
                7: 1.433e12,
                8: 2.872e12
                }

    while True:
        mensaje = "Numeración del primer objeto: "
        eleccion_1 = input_int(mensaje)

        if eleccion_1 <1 or eleccion_1 >8:
            print("Elección invalida.")
            continue

        else:
            break


    while True:
        mensaje = "Numeración del segundo objeto: "
        eleccion_2 = input_int(mensaje)

        if eleccion_2 == eleccion_1:
            print("No puedes elegir dos veces el mismo objeto.")
            continue

        elif eleccion_2 <1 or eleccion_2 >8:
            print("Elección invalida.\n")
            continue

        else:
            break

    d = abs(distancia[eleccion_1] - distancia[eleccion_2])

    G = 6.67430e-11

    m1 = cuerpos[eleccion_1]
    m2 = cuerpos[eleccion_2]

    ley_gravitacion_uni = G * m1 * m2 / d**2

    print(f"\nLa fuerza es de: {ley_gravitacion_uni:.2e} Newtons\n")

    print("El resultado en cuestión es una aproximación en base a la menor \n" \
    "distancia posible. Para mayor precisión, esperar a futuras versiones.\n")

    while True:
        print("1) Volver al incio\n" \
              "2) Salir\n")
    
        mensaje = "Introduce una opción (1/2): "
        opt = input_int(mensaje)

        if opt == 2:
            print("Saliendo...")
            break

        elif opt == 1:
            break

        else:
            print("Valor invalido.")
            print("Ingresa de nuevo tu elección.\n")
            continue
    
    print("\n================================================\n")