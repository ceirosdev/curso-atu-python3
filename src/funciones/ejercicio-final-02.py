"""
Desarrollar un programa que solicite la carga de tres valores y muestre el 
menor. Desde el bloque principal del programa llamar 2 veces a dicha función 
(sin utilizar una estructura repetitiva)
"""

def mayor_de_tres_enteros() -> int:
    numeros = []
    for i in range(1, 4):
        numeros.append(int(input(f"Ingresa el entero #{i}: ")))

    print(F"El mayor de los tres números es: {max(numeros)}")

if __name__ == "__main__":

    mayor_de_tres_enteros()

    print("")

    mayor_de_tres_enteros()
    