def filtrar_lista():
    lista_original = []
    NUM_ELEMENTOS = 5

    print("--- Carga de 5 enteros ---")
    
    # Paso 1: Cargar la lista con 5 elementos enteros
    for i in range(NUM_ELEMENTOS):
        while True:
            try:
                valor = int(input(f"Ingrese el entero número {i + 1}: "))
                lista_original.append(valor)
                break
            except ValueError:
                print("Error: Por favor, ingrese un número entero válido.")

    print("\nLista Original cargada:", lista_original)

    # Paso 2: Generar una nueva lista con los elementos que NO son mayores o iguales a 10
    # Usamos una comprensión de listas para filtrar: solo incluimos el 'elemento' 
    # si su valor es estrictamente MENOR que 10 (< 10).
    lista_filtrada = [elemento for elemento in lista_original if elemento < 10]

    # Paso 3: Imprimir la nueva lista
    print("\n--- Lista Filtrada (Elementos < 10) ---")
    print(lista_filtrada)

if __name__ == "__main__":
    filtrar_lista()
