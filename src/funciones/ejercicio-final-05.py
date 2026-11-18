"""
Elaborar una función que reciba tres enteros y nos retorne el valor promedio de 
los mismos.
"""

def promedio_de_tres_enteros(n1: int, n2: int, n3: int) -> float:
    return sum((n1, n2, n3)) / 3

def cargar_y_calcular_promedio() -> None:
    enteros = []
    for i in range(1, 4):
        enteros.append(int(input(f"Ingrese el entero #{i}: ")))

    promedio = promedio_de_tres_enteros(*enteros)

    print(f"\nEl promedio de los tres enteros es de {promedio:.2f}")

if __name__ == "__main__":

    cargar_y_calcular_promedio()
