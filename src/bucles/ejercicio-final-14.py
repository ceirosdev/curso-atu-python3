try:
    limite = int(input("Ingrese el valor máximo hasta el cual desea buscar múltiplos (ej: 500): "))
except ValueError:
    print("Por favor, ingrese un número entero válido para el límite.")

print(f"\n\tMúltiplos de 8 hasta {limite}")

multiplo = 8

while multiplo <= limite:
    print(multiplo)

    # Incrementar el múltiplo en 8 para obtener el siguiente
    multiplo = multiplo + 8
