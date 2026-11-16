"""
Definir una función que cargue una lista con palabras y la retorne. Luego otra 
función tiene que mostrar todas las palabras de la lista que tienen más de 5 
caracteres.
"""

# Devuelve una lista de palabras de una frase
def separar_palabras_de_frase(frase: str) -> list[str]:
    palabras = frase.split(" ")
    return palabras


# Toma una lista de palabras y muestra un grupo que cumpla un determinado 
# criterio
def palabras_criterio(longitud: int, palabras: list[str]) -> list[str]:
    palabras_nuevas = []

    for p in palabras:
        if len(p) >= longitud:
            palabras_nuevas.append(p)

    print(palabras_nuevas)


if __name__ == "__main__":
    
    palabras = separar_palabras_de_frase(
        input("Escriba su frase: ")
    )

    print("\tFrase dividida en palabras")
    print(palabras)

    print("\n\tFrase anterior dividida en palabras con longitud mayor que 5")
    palabras_criterio(longitud=5, palabras=palabras)
