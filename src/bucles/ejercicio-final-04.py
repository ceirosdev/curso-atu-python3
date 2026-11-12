while True:
    try:
        valor = int(input("Ingrese un número del 1 al 10: "))

        if 1 <= valor <= 10:
            break
        else:
            print("Error: El número debe estar estrictamente entre 1 y 10. Intente de nuevo.")

    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")


print(f"\nLa tabla del {valor}:")

for i in range(1, 11):

    resultado = valor * i
    print(f"{valor} x {i:2} = {resultado}")

