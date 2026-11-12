try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    minimo = num1

    if num2 < minimo:
        minimo = num2

    if num3 < minimo:
        minimo = num3

    maximo = num1

    if num2 > maximo:
        maximo = num2

    if num3 > maximo:
        maximo = num3

    print(f"El número menor es: {minimo}")
    print(f"El número mayor es: {maximo}")

except ValueError:
    print("Ingrese solo números enteros válidos.")
