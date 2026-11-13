def ordenar_nombres_paises():
    # Crear la lista con los nombres de 5 países
    paises = ["España", "México", "Argentina", "Chile", "Perú"]

    print("--- Lista Original de Países ---")
    print(paises)

    # Ordenar alfabéticamente la lista
    # Opción A: Usando el método .sort() (modifica la lista original)
    # paises.sort()

    # Opción B: Usando la función sorted() (crea una nueva lista ordenada, dejando la original intacta)
    paises_ordenados = sorted(paises)

    # Imprimir la lista ordenada
    print("\n--- Lista Ordenada Alfabéticamente ---")
    print(paises_ordenados)

if __name__ == "__main__":
    ordenar_nombres_paises()
