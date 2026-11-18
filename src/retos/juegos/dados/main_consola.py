
from dados import JuegoDados


def mostrar_resultado(resultado: dict):

    print("\n========== RESULTADOS ==========")

    print("\nJUGADOR:")
    print(f"Dados: {resultado['dados_jugador']}")
    print(f"Puntuación: {resultado['puntos_jugador']}")

    print("\nMÁQUINA:")
    print(f"Dados: {resultado['dados_maquina']}")
    print(f"Puntuación: {resultado['puntos_maquina']}")

    print("\n========== GANADOR ==========")

    if resultado["resultado"] == "ganador":
        print("¡Felicidades! Has ganado.")

    elif resultado["resultado"] == "perdedor":
        print("La máquina ha ganado. ¡Inténtalo de nuevo!")

    else:
        print("¡La partida ha terminado en empate!")

    print("===============================")


def main():

    juego = JuegoDados()

    print("================================")
    print("       JUEGO DE LOS DADOS")
    print("================================")

    while True:

        opcion = input(
            "\nPulsa ENTER para lanzar los dados "
            "o escribe 'salir' para terminar: "
        ).strip().lower()

        if opcion == "salir":
            print("\n¡Gracias por jugar!")
            break

        if opcion != "":
            print("Opción no válida.")
            continue

        resultado = juego.jugar_ronda()

        mostrar_resultado(resultado)


if __name__ == "__main__":
    main()
