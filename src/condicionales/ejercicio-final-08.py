try:
    mes = int(input("Ingrese el número del mes (1 a 12): "))
    dia = int(input("Ingrese el número del día (1 a 31): "))
    if mes == 12 and dia == 25:
        print("Esa fecha es Navidad.")
    else:
        print("Esa fecha no corresponde a Navidad.")

except ValueError:
    print("Por favor, ingrese solo números válidos para el mes y el día.")
