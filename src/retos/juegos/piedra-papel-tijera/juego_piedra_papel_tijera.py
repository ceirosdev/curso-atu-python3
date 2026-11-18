import random as opcion

def decisor():
    return opcion.randint(1, 3)


def maquina():
    return decisor()

def determinar_ganador(humano, pc):
    if humano == pc:
        return "empate"

    piedra, papel, tijera = 1, 2, 3

    if humano == piedra:

        if pc == tijera:
            return "humano"
    elif humano == papel:
        if pc == piedra:
            return "humano"

    elif humano == tijera:
        if pc == papel:
            return "humano"

    return "pc"


def juego(h_decision):
    if h_decision == 0:
        hum = decisor()
    else:
        hum = h_decision

    pc = maquina()

    resultado = determinar_ganador(hum, pc)

    if resultado == "empate":

        print("Ha habido un empate")
    elif resultado == "humano":

        print("El humano ha ganado")
    else:

        print("Ha ganado la pc")

def iniciar_juego():
    juegos_jugados = 0

    ganadas_humano = 0

    ganadas_pc = 0

    while True:
        print("\n--- Menú ---")

        print("1: Jugar")

        print("2: Salir")

        try:
            solicitud = int(input("Elija una opción: "))

            if solicitud == 2:
                break

            if solicitud == 1:

                juegos_jugados += 1

                print("\n--- Nuevo Juego ---")
                
                hum_decision = input("Elige: piedra (1), papel (2), tijera (3), decide por mí (0): ")
                hum_decision = int(hum_decision)

                juego(hum_decision)
                
                resultado = determinar_ganador(hum_decision if hum_decision != 0 else decisor(), maquina())

                if resultado == "humano":
                    ganadas_humano += 1
                else:
                    ganadas_pc += 1
            else:
                print("Opción no válida.")


        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

        if juegos_jugados >= 10:

            print("\n--- Tanteo Final ---")

            print(f"Total de juegos: {juegos_jugados}")

            print(f"Veces que ha ganado el humano: {ganadas_humano}")

            print(f"Veces que ha ganado la pc: {ganadas_pc}")

            break

if __name__ == "__main__":

    iniciar_juego()

