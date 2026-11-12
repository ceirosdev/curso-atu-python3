try:
    x = int(input("Ingrese la coordenada X: "))
    y = int(input("Ingrese la coordenada Y: "))
    
    if x > 0 and y > 0:
        print("El punto se ubica en el Primer Cuadrante.")
    elif x < 0 and y > 0:
        print("El punto se ubica en el Segundo Cuadrante.")
    elif x < 0 and y < 0:
        print("El punto se ubica en el Tercer Cuadrante.")
    elif x > 0 and y < 0:
        print("El punto se ubica en el Cuarto Cuadrante.")
    else:
        print("Las coordenadas ingresadas no definen un cuadrante.")

except ValueError:
    print("Ingrese valores enteros válidos para las coordenadas.")
