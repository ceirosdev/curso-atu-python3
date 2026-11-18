
import random as opcion


# Generar una decisión aleatoria
def decisor() -> int:
    return opcion.randint(1, 3)


# Decisión de la máquina
def maquina() -> int:
    return decisor()


# Determinar el ganador
def determinar_ganador(humano: int, pc: int) -> str:

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


# Ejecutar una partida
def juego(h_decision: int = 0) -> dict:

    # Si la decisión es 0, el programa decide por el humano
    if h_decision == 0:
        hum = decisor()
    else:
        hum = h_decision

    pc = maquina()

    resultado = determinar_ganador(hum, pc)

    return {
        "humano": hum,
        "pc": pc,
        "resultado": resultado
    }
