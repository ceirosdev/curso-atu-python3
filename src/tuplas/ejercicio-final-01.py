# ejercicio-final-01

"""
Confeccionar un programa con las siguientes funciones:
1) Cargar una lista de 5 enteros.
2) Retornar el mayor y menor valor de la lista mediante una tupla. Desempaquetar 
la tupla en el bloque principal y mostrar el mayor y menor.
"""

numeros = []

for i in range(1, 6):
    # numeros[-1:] += [int(input(f"Ingrese el número {i}: "))]
    numeros.append(int(input(f"Ingrese el número {i}: ")))

num_inmutables = tuple(numeros)

print(f"\nLa lista de números es: {num_inmutables}")

print(f"\nEl mayor elemento del listado es: {max(num_inmutables)}")
print(f"El menor elemento del listado es: {min(num_inmutables)}")
