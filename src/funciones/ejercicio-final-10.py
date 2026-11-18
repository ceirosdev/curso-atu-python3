"""
Desarrollar una función que reciba una lista de string y nos retorne el que 
tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres debe 
retornar el que tiene un valor de componente más baja. En el bloque principal 
iniciamos por asignación la lista de string:
"""

def mas_caracteres(palabras: list[str]) -> str:
    palabra = ""
    cant_caracteres = 0

    for caracter in palabras:
        # Obtener la cantidad de caracteres de la palabra actual
        tam_caracter = len(caracter)

        # Guarda el caracter con mayor tamaño y su nombre
        if cant_caracteres < tam_caracter:
            cant_caracteres = tam_caracter
            palabra = caracter

    return palabra

if __name__ == "__main__":

    capitales = ["Londres", "Moscú", "La Habana", "Santo Domingo", "Sofía"]

    # Imprimirá 'Santo Domingo'
    print(mas_caracteres(capitales))
