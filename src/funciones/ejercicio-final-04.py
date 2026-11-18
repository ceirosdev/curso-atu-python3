"""
Confeccionar una función que reciba tres enteros y los muestre ordenados de 
menor a mayor. En otra función solicitar la carga de 3 enteros por teclado y 
proceder a llamar a la primer función definida.
"""

# Toma tres números enteros y los devuevle en una lista ordenada
def ordenar_tres_enteros(n1: int, n2: int, n3: int) -> list[int]:
    return sorted([n1, n2, n3])

def carga_de_tres_enteros_y_ordenarlos() -> None:
    
    enteros_desordenados = []

    # Obtiene los tres enteros desordenados
    for i in range(1, 4):
        enteros_desordenados.append(int(input(f"Ingrese el entero #[{i}]: ")))

    # Desempaqueta los enteros desordenados y los guarda ordenados
    enteros_ordenados = ordenar_tres_enteros(*enteros_desordenados)

    print("\n\tMostrar enteros ordenados")

    for i in enteros_ordenados:
        print(f"{i}", end=" ")


if __name__ == "__main__":

    carga_de_tres_enteros_y_ordenarlos()
