# La lista original de listas
lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]

# Imprimir la lista original
print("--- Lista Original ---")
print(lista)
print("-" * 30)

# Fijar con el valor cero todos los elementos mayores a 50
# Necesitamos un bucle anidado: uno para recorrer las listas internas, y otro para modificar los elementos.

for sublista in lista:
    # Iteramos sobre cada elemento dentro de la sublista actual
    for i in range(len(sublista)):
        elemento = sublista[i]
        
        # Verificamos la condición: si el elemento es mayor a 50
        if elemento > 50:
            # Reemplazamos el elemento por cero
            sublista[i] = 0

# Volver a imprimir la lista modificada
print("\n--- Lista Modificada (Elementos > 50 cambiados a 0) ---")
print(lista)
