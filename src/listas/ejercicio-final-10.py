def sumar_listas():
    LISTA_SIZE = 4
    lista_a = []
    lista_b = []

    print("--- Carga de la Lista 1 (4 enteros) ---")
    for i in range(LISTA_SIZE):
        while True:
            try:
                valor = int(input(f"Ingrese el elemento {i + 1} de la Lista 1: "))
                lista_a.append(valor)
                break
            except ValueError:
                print("Error: Por favor, ingrese un número entero válido.")

    print("\n--- Carga de la Lista 2 (4 enteros) ---")
    for i in range(LISTA_SIZE):
        while True:
            try:
                valor = int(input(f"Ingrese el elemento {i + 1} de la Lista 2: "))
                lista_b.append(valor)
                break
            except ValueError:
                print("Error: Por favor, ingrese un número entero válido.")

    # Generar la tercera lista (suma de elementos en la misma posición)
    # Usamos comprensión de listas para hacer esto de forma concisa.
    lista_suma = [lista_a[i] + lista_b[i] for i in range(LISTA_SIZE)]

    # Mostrar la tercera lista
    print("--- RESULTADO ---")
    print(f"Lista A ingresada: {lista_a}")
    print(f"Lista B ingresada: {lista_b}")
    print("\nLista de sumas (Posición i de Lista A + Lista B):")
    print(lista_suma)

if __name__ == "__main__":
    sumar_listas()
