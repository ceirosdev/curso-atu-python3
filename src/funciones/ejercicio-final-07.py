"""
Confeccionar una función que calcule la superficie de un rectángulo y la 
retorne, la función recibe como parámetros los valores de dos de sus lados: 
En el bloque principal del programa cargar los lados de dos rectángulos y luego 
mostrar cual de los dos tiene una superficie mayor.
"""

# Calcula la superficie de un rectámgulo
def superficie_rectangulo(
    l_ancho: float,
    l_largo: float
) -> float:
    return l_ancho * l_largo

# Muestra el rectángulo que tiene mayor suerficie
def comparar_superficie_rectangulos() -> None:
    lados1, lados2 = [], []

    print("\tCargar lados del primer rectángulo")

    for i in range(1, 3):
        lados1.append(float(input(f"Cargar el lado {i} "
                                  + "del primer rectángulo: ")))

    print("\n\tCargar lados del segundo rectángulo")

    for i in range(1, 3):
        lados2.append(float(input("Cargar el lado "
                                  + f"{i} del segundo rectángulo: ")))

    # Calcula las superficies de los dos rectángulos
    superf_rectangulo1 = superficie_rectangulo(*lados1)
    superf_rectangulo2 = superficie_rectangulo(*lados2)

    # Muestra cuál de los dos rectángulos tienen la mayor superficie
    if superf_rectangulo1 == superf_rectangulo2:

        print("\nLos rectángulos tienen la misma superficie de "
              + f"{superf_rectangulo1:.2f} u^2.")
        
    elif superf_rectangulo1 > superf_rectangulo2:
        
        print("\nEl primer rectángulo tiene la mayor superficie de " 
              + f"{superf_rectangulo1:.2f} u^2 frente al segundo con " 
              + f"{superf_rectangulo2:.2f} u^2.")

    else:
        print("\nEl segundo rectángulo tiene la mayor superficie de " 
                      + f"{superf_rectangulo2:.2f} u^2 frente al primero con " 
                      + f"{superf_rectangulo1:.2f} u^2.")

if __name__ == "__main__":

    comparar_superficie_rectangulos()
