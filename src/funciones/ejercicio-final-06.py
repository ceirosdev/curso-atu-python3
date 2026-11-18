"""
Elaborar una función que nos retorne el perímetro de un cuadrado pasando como 
parámetros el valor de un lado.
"""

def perimetro_del_cuadrado(lado: float) -> float:
    return 4 * lado

if __name__ == "__main__":

    perimetro = perimetro_del_cuadrado(lado=3.4)
    
    print(perimetro)
