numero = int(input("Ingresa un número entre [1 - 99]: "))

if numero < 1:
    print("No se admiten números menores que 1")
elif numero > 99:
    print("No se admiten números mayores que 99")
elif numero >= 10:
    print(f'El número {numero} tiene dos dígitos')
else:
    print(f'El número {numero} tiene un dígito')

# Salida 1:
# Ingresa un número entre [1 - 99]: 0
# No se admiten números menores que 1

# Salida 2:
# Ingresa un número entre [1 - 99]: 1
# El número 1 tiene un dígito

# Salida 3:
# Ingresa un número entre [1 - 99]: 10
# El número 10 tiene dos dígitos

# Salida 4
# Ingresa un número entre [1 - 99]: 100
# No se admiten números mayores que 99