def obtener_ultimo_elemento():
    # Crear una lista por asignación con la cantidad de elementos deseada
    lista_principal = [
        [1, 2],          # Sublista 0
        [3, 4, 5],       # Sublista 1
        ['a', 'b', 'c']  # Sublista 2
    ]

    print("--- Lista Principal Creada ---")
    print(lista_principal)

    # Imprimir el último elemento de la lista principal
    # Usamos el índice -1 para acceder al último elemento de cualquier lista en Python.
    ultimo_elemento = lista_principal[-1]
    
    print(f"El último elemento de la lista principal es: {ultimo_elemento}")

if __name__ == "__main__":
    obtener_ultimo_elemento()
