"""
Definir una lista de enteros por asignación en el bloque principal. Llamar a una 
función que reciba la lista y nos retorne el producto de todos sus elementos. 
Mostrar dicho producto en el bloque principal de nuestro programa.
"""

def producto_de_lista(numeros: list[int]) -> int:

    prod_actual = 1

    for numero in numeros:
        prod_actual *= numero

    return prod_actual

def calcular_producto_de_lista() -> None:
    
    enteros = [1, 2, 3, 4, 5]
    producto = producto_de_lista(numeros=enteros)

    print(f"El producto de todos los elementos de la lista es de {producto}.")


if __name__ == "__main__":

    calcular_producto_de_lista()
