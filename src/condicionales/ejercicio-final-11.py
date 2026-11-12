try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    if num1 == num2 and num2 == num3:
        resultado = (num1 + num2) * num3
        print(f"Todos los números son iguales. El resultado es: {resultado}")
    else:
        print("Los números ingresados no son iguales. No se realiza el cálculo.")

except ValueError:
    print("Por favor, ingrese solo números enteros válidos.")
