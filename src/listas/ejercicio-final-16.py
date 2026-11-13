# La lista original de listas
lista = [[4, 12, 5, 66], [14, 6, 25], [3, 4, 5, 67, 89, 23, 1], [78, 56]]

# Imprimir la lista original
print("--- Lista Original ---")
print(lista)

# Fijar con el valor cero todos los elementos mayores a 10
# Necesitamos dos bucles: uno para la lista externa y otro para cada sublista.

for sublista in lista:
    # Iteramos sobre cada elemento dentro de la sublista actual
    for i in range(len(sublista)):
        elemento = sublista[i]

        # Verificamos la condición: si el elemento es mayor a 10
        if elemento > 10:
            # Reemplazamos el elemento por cero, modificando la lista original
            sublista[i] = 0

# Volver a imprimir la lista modificada
print("\n--- Lista Modificada (Elementos > 10 cambiados a 0) ---")
print(lista)
