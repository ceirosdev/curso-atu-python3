# Inicialización de contadores y acumulador
negativos_count = 0
positivos_count = 0
multiplos_15_count = 0
suma_pares = 0

# Bucle for para procesar exactamente 10 valores
for i in range(10):
    try:
        # Solicitamos el valor al usuario y lo convertimos a entero
        valor = int(input(f"Ingrese el valor {i + 1} de 10: "))

        # a) Contar negativos
        if valor < 0:
            negativos_count += 1

        # b) Contar positivos
        elif valor > 0:
            positivos_count += 1

        # c) Contar múltiplos de 15
        if valor % 15 == 0:
            multiplos_15_count += 1

        # d) Acumular números pares
        if valor % 2 == 0:
            suma_pares += valor

    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese un número entero.")
        # Si hay un error de entrada, simplemente saltamos a la siguiente iteración del bucle
        continue

# a) Cantidad de negativos
print(f"a) Cantidad de valores negativos: {negativos_count}")

# b) Cantidad de positivos
print(f"b) Cantidad de valores positivos: {positivos_count}")

# c) Cantidad de múltiplos de 15
print(f"c) Cantidad de múltiplos de 15: {multiplos_15_count}")

# d) Valor acumulado de los números pares
print(f"d) Suma acumulada de los números pares: {suma_pares}")
