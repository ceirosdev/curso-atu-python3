num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))


if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

print(f"El número mayor es: {mayor}")

# Salida:

# Número 1: 7
# Número 2: 9
# Número 3: 6
# El número mayor es: 9