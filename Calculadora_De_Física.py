def input_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        
        except ValueError:
            print("Error: Ingresa un número válido.")

def input_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        
        except ValueError:
            print("Error: Ingresa un número entero.")

def newton_2():
    while True:
        print("\nIngrese la masa en kilogramos (kg) y la aceleración")
        print("en metros por segundo cuadrado (m/s²)\n")

        mensaje = "Ingrese la masa: "

        masa = input_float(mensaje)

        if masa <= 0:
            print("La masa no puede ser negativa o cero.")
            continue

        else:
            mensaje = "Ingrese la aceleracion: "
            aceleracion = input_float(mensaje)
            fuerza = masa * aceleracion

            print(f"\nFuerza: {fuerza:.2f} Newtons")
            historial.append(f"2ª Ley: {masa} kg x {aceleracion} m/s² = {fuerza:.2f} N")
            break

def cinetica():
    while True:
        print("\nIngrese la masa en kilogramo (kg) y la")
        print("velocidad en metros por segundo (m/s)\n")

        mensaje = "Ingrese la masa: "
        masa = input_float(mensaje)

        if masa <= 0:
            print("La masa no puede ser negativa o cero.")
            continue

        else:
            mensaje = "Ingrese la velocidad: "
            velocidad = input_float(mensaje)
            energia = 0.5 * masa * (velocidad ** 2)

            print(f"\nEnergía cinética: {energia:.2f} Joules")
            historial.append(f"Energía cinética: 0.5 x {masa} x ({velocidad}²) = {energia:.2f} J")
            break


def menu_2():
    print("\n 1) Sacar distancia")
    print(" 2) Sacar velocidad")
    print(" 3) Sacar tiempo")
    print(" 4) Salir\n")

    mensaje = "Ingresa una opción (1/2/3/4): "
    opt_2 = input_int(mensaje)

    if opt_2 == 1:
        while True:
            print("\nDescribe la velocidad en metro por segundo (m/s)")
            print("y el tiempo en segundos (s).\n")

            mensaje = "Ingresa la velocidad: "

            velocidad = input_float(mensaje)

            mensaje = "Ingresa el tiempo: "
            tiempo = input_float(mensaje)

            if tiempo <= 0:
                print("El tiempo no puede ser negativo o cero.")
                continue

            else:
                distancia = velocidad * tiempo
                print(f"\nDistancia: {distancia:.2f} m")
                historial.append(f"Distancia: {velocidad} x {tiempo} = {distancia} m")
                break


    elif opt_2 == 2:
        while True:
            print("\nDescribe la distancia en metro (m)")
            print("y el tiempo en segundos (s).\n")

            mensaje = "Ingrese la distancia: "
            distancia = input_float(mensaje)

            mensaje = "Ingrese el tiempo: "
            tiempo = input_float(mensaje)

            if tiempo <= 0:
                print("El tiempo no puede ser 0 o menor.")
                continue

            else:
                velocidad = distancia / tiempo
                print(f"\nVelocidad: {velocidad:.2f} m/s")

                historial.append(f"Velocidad: {distancia} / {tiempo} = {velocidad} m/s")
                break


    elif opt_2 == 3:
        while True:
            print("\nDescribe la distancia en metro (m) y la")
            print("velocidad en metros por segundo (m/s).\n")

            mensaje = "Ingrese la distancia: "
            distancia = input_float(mensaje)

            mensaje = "Ingrese la velocidad: "
            velocidad = input_float(mensaje)

            if velocidad == 0:
                print("La velocidad no puede ser 0.")
                continue

            else:
                tiempo = distancia / velocidad

                print(f"\nTiempo: {tiempo:.2f} s")
                historial.append(f"Tiempo: {distancia} / {velocidad} = {tiempo:.2f} s")
                break


historial = []

print("\n=====================MENÚ DE INICIO=====================\n")

print(" 1) Movimiento Rectilíneo Uniforme")
print(" 2) Segunda Ley de Newton")
print(" 3) Energía Cinética")
print(" 4) Historial")
print(" 5) Salir\n")

mensaje = "Introduce una opción (1/2/3/4/5): "
opt = input_int(mensaje)

while opt != 5:

    match opt:
        case 1:
            menu_2()

        case 2:
            newton_2()

        case 3:
            cinetica()

        case 4:
            if not historial:
                print("\nNo hay cálculos registrados.")

            else:
                print("\n------------ Historial de cálculos ------------\n")
            
                for idx, calc in enumerate(historial, 1):
                    print(f"{idx}. {calc}")

                print("\n-----------------------------------------------\n")
                input("Presiona Enter para continuar...")
            
        case _:
            print("Opción invalida. \n" \
            "Intente de nuevo")

    print("\n=====================MENÚ DE INICIO=====================\n")

    print(" 1) Movimiento Rectilíneo Uniforme")
    print(" 2) Segunda Ley de Newton")
    print(" 3) Energía Cinética")
    print(" 4) Historial")
    print(" 5) Salir\n")

    mensaje = "Introduce una opción (1/2/3/4/5): "
    opt = input_int(mensaje)