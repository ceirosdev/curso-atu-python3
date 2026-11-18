"""
Crear una lista de enteros por asignación. Definir una función que reciba una 
lista de enteros y un segundo parámetro de tipo entero. Dentro de la función 
mostrar cada elemento de la lista multiplicado por el valor entero enviado.
"""

def multiplacar_lista_por(numero: float, lista: list) -> list:
    lista_modificada = []

    for i in range(len(lista)):
        lista_modificada.append(lista[i] * numero)

    return lista_modificada

if __name__ == "__main__":
    lista = [3.14, 4, 7, 2]

    print(multiplacar_lista_por(numero=3, lista=lista))
    