try:
    dia_numero = int(input("Ingrese un número del 1 al 7 para seleccionar el día: "))

    if dia_numero == 1:
        print("El día es: Lunes")
    elif dia_numero == 2:
        print("El día es: Martes")
    elif dia_numero == 3:
        print("El día es: Miércoles")
    elif dia_numero == 4:
        print("El día es: Jueves")
    elif dia_numero == 5:
        print("El día es: Viernes")
    elif dia_numero == 6:
        print("El día es: Sábado")
    elif dia_numero == 7:
        print("El día es: Domingo")
    else:
        print("Ingrese un número válido entre 1 y 7.")
except ValueError:
    print("Ingrese solo números enteros.")
