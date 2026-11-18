
import random

from palabras import PALABRAS


# Seleccionar una palabra de manera aleatoria
def sel_palabra() -> str:
    return random.choice(PALABRAS)


# Lógica para adivinar la palabra
def adivinar_palabra(intentos: int):

    # Se selecciona la palabra de manera aleatoria
    palabra = sel_palabra()
    longitud = len(palabra)

    # Se guarda en una lista cada carácter para adivinar
    progreso = list("_" * longitud)

    # Guardar las letras introducidas
    letras_introducidas = []

    contar_int = intentos

    while contar_int > 0:

        print(" ".join(progreso))

        letra = input(
            f"\n[Intentos: {contar_int}] Escriba una letra: "
        ).lower().strip()

        # Comprobar que se ha introducido una sola letra
        if len(letra) != 1 or not letra.isalpha():
            print("Introduce solamente una letra.")
            continue

        # Comprobar si la letra ya fue introducida
        if letra in letras_introducidas:
            print("Ya has introducido esa letra.")
            continue

        letras_introducidas.append(letra)

        # Comprobar si la letra pertenece a la palabra
        encontrada = False

        for indice, caracter in enumerate(palabra):

            if letra == caracter:
                progreso[indice] = caracter
                encontrada = True

        print("")

        if progreso == list(palabra):
            print(
                f"¡Felicidades! Has adivinado la palabra '{palabra}'."
            )
            break

        if not encontrada:
            contar_int -= 1

        if contar_int == 0:
            print(
                f"¡Lo lamento! No has adivinado la palabra '{palabra}'."
            )


if __name__ == "__main__":
    adivinar_palabra(8)
