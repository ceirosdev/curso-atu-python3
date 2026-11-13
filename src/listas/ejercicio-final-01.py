# 1. Definir la lista con 8 elementos enteros
numeros = [50, 120, 99, 300, 100, 85, 200, 1]

# Inicializar el contador
conteo = 0

# Iterar sobre la lista
for numero in numeros:
    # Verificar si el número es superior a 100
    if numero > 100:
        conteo += 1

# Imprimir el resultado
print(f"La lista definida es: {numeros}")
print(f"El número de elementos superiores a 100 es: {conteo}")
