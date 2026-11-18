"""
Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores 
positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""

def cargar_lista():

    enteros = []

    for i in range(1, 11):
        enteros.append(int(input(f"Elemento {i}: ")))

    return enteros

def filtrar_positivos(entero: list[int]) -> list[int]:
    positivos = []

    for i in entero:
        if i >= 0:
            positivos.append(i)

    return positivos

def filtrar_negativos(entero: list[int]) -> list[int]:
    negativos = []

    for i in entero:
        if i < 0:
            negativos.append(i)

    return negativos

if __name__ == "__main__":

    enteros = cargar_lista()
    print(enteros)

    positivos = filtrar_positivos(enteros)
    print(positivos)

    negativos = filtrar_negativos(enteros)
    print(negativos)
