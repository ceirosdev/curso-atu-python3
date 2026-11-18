
import random


class JuegoDados:

    def __init__(self):
        self.dados_jugador = []
        self.dados_maquina = []

        self.puntos_jugador = 0
        self.puntos_maquina = 0

    # Lanzar dos dados
    def lanzar_dados(self) -> list:
        return [
            random.randint(1, 6),
            random.randint(1, 6)
        ]

    # Jugar una ronda
    def jugar_ronda(self) -> dict:

        # Lanzamiento del jugador
        self.dados_jugador = self.lanzar_dados()

        # Lanzamiento de la máquina
        self.dados_maquina = self.lanzar_dados()

        # Calcular las puntuaciones
        self.puntos_jugador = sum(self.dados_jugador)
        self.puntos_maquina = sum(self.dados_maquina)

        # Determinar el resultado
        if self.puntos_jugador > self.puntos_maquina:
            resultado = "ganador"

        elif self.puntos_jugador < self.puntos_maquina:
            resultado = "perdedor"

        else:
            resultado = "empate"

        # Devolver los resultados de la ronda
        return {
            "dados_jugador": self.dados_jugador,
            "dados_maquina": self.dados_maquina,
            "puntos_jugador": self.puntos_jugador,
            "puntos_maquina": self.puntos_maquina,
            "resultado": resultado
        }
