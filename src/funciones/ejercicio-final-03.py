"""
Desarrollar una funcion que reciba un string como parametro y nos muestre la 
cantidad de vocales. Llamarla desde el bloque principal del programa 3 veces con 
string distintos.
"""

def contar_vocales_de_frase(frase: str):
    conteo = 0
    # Normaliza y recorre caracter por caracter
    for i in frase.lower():
        # Hará el conteo si el caracter actual es una vocal
        if i in ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']:
            conteo +=1

    return conteo

if __name__ == "__main__":

    # Cuenta 8 vocales
    print(contar_vocales_de_frase("ahora es el momento"))

    # Cuenta 11 vocales
    print(contar_vocales_de_frase("no dejes las cosas para después"))
