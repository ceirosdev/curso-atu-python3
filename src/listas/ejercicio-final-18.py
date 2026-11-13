def gestionar_empleados():
    # Solicitar la cantidad de empleados
    while True:
        try:
            cantidad_str = input("Ingrese la cantidad de empleados que tiene la empresa: ")
            cantidad = int(cantidad_str)
            if cantidad > 0:
                break
            else:
                print("Por favor, ingrese un número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    nombres = []
    sueldos = []

    print(f"\n--- Ingreso de datos para {cantidad} empleados ---")

    # Cargar los nombres y sueldos
    for i in range(cantidad):
        # Ingreso del nombre
        nombre = input(f"Ingrese el nombre del empleado {i + 1}: ")
        nombres.append(nombre)

        # Ingreso del sueldo (con validación de entrada numérica)
        while True:
            try:
                sueldo = float(input(f"Ingrese el sueldo de {nombre}: "))
                sueldos.append(sueldo)
                break
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido para el sueldo.")

    print("--- LISTAS ORIGINALES ---")
    print(f"Nombres originales: {nombres}")
    print(f"Sueldos originales: {sueldos}")

    # Filtrar: Crear nuevas listas solo con empleados cuyo sueldo sea <= 10000
    nombres_filtrados = []
    sueldos_filtrados = []

    # Usamos zip para recorrer ambas listas al mismo tiempo
    for nombre, sueldo in zip(nombres, sueldos):
        # Si el sueldo es MENOR O IGUAL a 10000, lo incluimos en las listas filtradas
        if sueldo <= 10000:
            nombres_filtrados.append(nombre)
            sueldos_filtrados.append(sueldo)

    # Imprimir los resultados filtrados
    print("\n--- LISTAS FILTRADAS (Sueldo <= 10000) ---")
    print(f"Nombres filtrados: {nombres_filtrados}")
    print(f"Sueldos filtrados: {sueldos_filtrados}")


if __name__ == "__main__":
    gestionar_empleados()
