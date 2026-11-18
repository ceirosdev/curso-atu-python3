
import random

from palabras import PALABRAS


class Ahorcado:

    def __init__(self, intentos: int = 8):
        self.intentos_maximos = intentos
        self.reiniciar_partida()

    # Seleccionar una palabra aleatoria
    def sel_palabra(self) -> str:
        return random.choice(PALABRAS)

    # Inicializar o reiniciar la partida
    def reiniciar_partida(self):

        self.palabra = self.sel_palabra()

        self.progreso = ["_"] * len(self.palabra)

        self.letras_introducidas = []

        self.intentos_restantes = self.intentos_maximos

        self.ganada = False
        self.perdida = False

    # Comprobar una letra introducida
    def adivinar_letra(self, letra: str) -> dict:

        letra = letra.lower().strip()

        # Comprobar si la partida ha terminado
        if self.ganada or self.perdida:
            return {
                "estado": "terminada",
                "mensaje": "La partida ya ha terminado."
            }

        # Validar que se introduzca una sola letra
        if len(letra) != 1 or not letra.isalpha():
            return {
                "estado": "invalida",
                "mensaje": "Introduce una sola letra válida."
            }

        # Comprobar si la letra ya fue introducida
        if letra in self.letras_introducidas:
            return {
                "estado": "repetida",
                "mensaje": "Ya has introducido esa letra."
            }

        self.letras_introducidas.append(letra)

        # Comprobar si la letra pertenece a la palabra
        encontrada = False

        for indice, caracter in enumerate(self.palabra):

            if letra == caracter:
                self.progreso[indice] = caracter
                encontrada = True

        # Comprobar si el jugador ha ganado
        if self.progreso == list(self.palabra):

            self.ganada = True

            return {
                "estado": "ganada",
                "mensaje": "¡Felicidades! Has adivinado la palabra."
            }

        # Si la letra no pertenece a la palabra, descontar un intento
        if not encontrada:

            self.intentos_restantes -= 1

            # Comprobar si el jugador ha perdido
            if self.intentos_restantes == 0:

                self.perdida = True

                return {
                    "estado": "perdida",
                    "mensaje": "¡Lo sentimos! Te has quedado sin intentos."
                }

            return {
                "estado": "error",
                "mensaje": "La letra no se encuentra en la palabra."
            }

        return {
            "estado": "acierto",
            "mensaje": "¡Muy bien! Has encontrado una letra."
        }

    # Obtener el progreso actual de la palabra
    def obtener_progreso(self) -> str:
        return " ".join(self.progreso)

    # Obtener las letras introducidas
    def obtener_letras_introducidas(self) -> list:
        return self.letras_introducidas.copy()

    # Comprobar si la partida ha terminado
    def partida_terminada(self) -> bool:
        return self.ganada or self.perdida


if __name__ == "__main__":

    juego = Ahorcado()

    while not juego.partida_terminada():

        print("\n", juego.obtener_progreso())
        print("Intentos:", juego.intentos_restantes)

        letra = input("Introduce una letra: ")

        resultado = juego.adivinar_letra(letra)

        print(resultado["mensaje"])

    if juego.ganada:
        print("¡Has ganado!")

    else:
        print("¡Has perdido!")
        print("La palabra era:", juego.palabra)
