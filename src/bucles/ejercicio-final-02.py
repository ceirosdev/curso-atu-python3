numeros = []

for i in range(10):
    while True:
        try:
            numero = float(input(f"Ingrese el número {i + 1} de 10: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

ultimos_cinco = numeros[-5:]

suma_ultimos_cinco = sum(ultimos_cinco)

print("Los últimos 5 valores ingresados son:", ultimos_cinco)
print(f"La suma de los últimos 5 valores es: {suma_ultimos_cinco}")
