
"""
Se tiene que cargar los votos obtenidos por tres candidatos a una elección.

1) Mostrar el nombre de cada candidato y la cantidad total de votos.
2) Mostrar el candidato ganador.
"""

# Datos definidos estáticamente
candidatos = [
    ("juan", [("cordoba", 100), ("buenos aires", 200)]),
    ("ana", [("cordoba", 55)]),
    ("luis", [("buenos aires", 20)])
]


def mostrar_info_candidatos(
    cand: list[tuple[str, list[tuple[str, int]]]]
) -> None:

    for nombre, provincias in cand:

        total_votos = 0

        for _, votos in provincias:
            total_votos += votos

        print(f"Candidato: {nombre}")
        print(f"Total de votos: {total_votos}")
        print("-" * 30)


def mostrar_candidato_ganador(
    cand: list[tuple[str, list[tuple[str, int]]]]
) -> None:

    candidato_ganador = ""
    max_votos = -1

    for nombre, provincias in cand:

        total_votos = 0

        for _, votos in provincias:
            total_votos += votos

        if total_votos > max_votos:
            max_votos = total_votos
            candidato_ganador = nombre

    print(f"Candidato ganador: {candidato_ganador}")
    print(f"Total de votos: {max_votos}")


if __name__ == "__main__":

    print("\tMostrar información de los candidatos")
    mostrar_info_candidatos(candidatos)

    print("\n\tMostrar el candidato ganador")
    mostrar_candidato_ganador(candidatos)
