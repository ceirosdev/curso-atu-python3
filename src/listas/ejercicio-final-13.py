def ordenar_lista_dos_maneras():
    # Crear la lista con 5 elementos enteros
    numeros = [50, 120, 30, 90, 100]

    print("--- Lista Original ---")
    print(f"Lista inicial: {numeros}")

    # Ordenar de menor a mayor (Ascendente)
    # Usamos .sort() para modificar la lista original
    numeros.sort()

    print("Lista ordenada de menor a mayor:")
    print(numeros)

    # Ordenar de mayor a menor (Descendente)
    # Usamos .sort() con el argumento reverse=True
    numeros.sort(reverse=True)

    print("Lista ordenada de mayor a menor:")
    print(numeros)

if __name__ == "__main__":
    ordenar_lista_dos_maneras()
