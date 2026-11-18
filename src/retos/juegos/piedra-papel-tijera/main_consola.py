
from juego_piedra_papel_tijera_para_ui import juego


def iniciar_juego():

    juegos_jugados = 0
    ganadas_humano = 0
    ganadas_pc = 0
    empates = 0

    while juegos_jugados < 10:

        print("\n--- MENÚ ---")
        print("1: Jugar")
        print("2: Salir")

        try:

            solicitud = int(input("Elija una opción: "))

            if solicitud == 2:
                break

            if solicitud != 1:
                print("Opción no válida.")
                continue

            print("\n--- NUEVO JUEGO ---")

            print("1: Piedra")
            print("2: Papel")
            print("3: Tijera")
            print("0: Decide por mí")

            hum_decision = int(
                input("Elige una opción: ")
            )

            if hum_decision not in (0, 1, 2, 3):
                print("Decisión no válida.")
                continue

            # Ejecutar una sola partida
            resultado = juego(hum_decision)

            juegos_jugados += 1

            # Mostrar las decisiones
            opciones = {
                1: "Piedra",
                2: "Papel",
                3: "Tijera"
            }

            print(
                f"\nHumano: {opciones[resultado['humano']]}"
            )

            print(
                f"Máquina: {opciones[resultado['pc']]}"
            )

            # Actualizar el marcador
            if resultado["resultado"] == "humano":

                print("¡El humano ha ganado!")
                ganadas_humano += 1

            elif resultado["resultado"] == "pc":

                print("¡La máquina ha ganado!")
                ganadas_pc += 1

            else:

                print("¡Ha habido un empate!")
                empates += 1

        except ValueError:

            print("Entrada inválida. Introduce un número.")

    # Mostrar resultados finales
    print("\n--- TANTEO FINAL ---")

    print(f"Total de juegos: {juegos_jugados}")
    print(f"Victorias del humano: {ganadas_humano}")
    print(f"Victorias de la máquina: {ganadas_pc}")
    print(f"Empates: {empates}")

    print("\n¡Gracias por jugar!")


if __name__ == "__main__":
    iniciar_juego()
