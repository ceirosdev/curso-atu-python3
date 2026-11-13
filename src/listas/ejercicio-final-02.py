# 1. Definir una lista con 5 enteros
mi_lista = [4, 10, 8, 25, 6]

print("Elementos de la lista:")
print(mi_lista)
print("-" * 30)

# 2. Iterar sobre la lista y mostrar solo los elementos que cumplen la condición
print("Elementos iguales o superiores a 7:")

for numero in mi_lista:
    # Verificar si el valor es mayor o igual a 7
    if numero >= 7:
        print(numero)
