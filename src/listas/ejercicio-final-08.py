def gestionar_productos():
    nombres = []
    precios = []
    NUM_PRODUCTOS = 5

    print("--- Carga de Productos ---")

    # Crear y cargar las dos listas paralelas
    for i in range(NUM_PRODUCTOS):
        # Cargar nombre
        nombre = input(f"Ingrese el nombre del producto {i + 1}: ")
        nombres.append(nombre)

        # Cargar precio (con validación de entrada numérica)
        while True:
            try:
                precio = float(input(f"Ingrese el precio del producto '{nombre}': "))
                precios.append(precio)
                break
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido para el precio.")

    # Mostrar las listas
    print("--- LISTAS ALMACENADAS ---")
    print(f"Nombres de los productos: {nombres}")
    print(f"Precios de los productos: {precios}")

    # Definir el precio del primer producto
    if not precios:
        print("Error: La lista de precios está vacía. No se puede realizar el análisis.")
        return

    primer_precio = precios[0]
    print(f"\nEl precio del primer producto es: {primer_precio:.2f}")

    # Contar productos con precio mayor
    contador_mayores = 0
    for precio in precios:
        if precio > primer_precio:
            contador_mayores += 1

    # Mostrar el resultado final
    print("--- Resultado del Análisis ---")
    print(f"Cantidad de productos con precio mayor al primer producto: {contador_mayores}")


if __name__ == "__main__":
    gestionar_productos()
