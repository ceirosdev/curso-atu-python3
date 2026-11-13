def ordenar_sueldos():
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

    sueldos = []
    print(f"\n--- Carga de {cantidad} sueldos ---")

    # Crear y cargar la lista con todos los sueldos
    for i in range(cantidad):
        while True:
            try:
                sueldo = float(input(f"Ingrese el sueldo del empleado {i + 1}: "))
                sueldos.append(sueldo)
                break
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido para el sueldo.")

    # Ordenar la lista de sueldos de menor a mayor
    sueldos.sort()

    # Imprimir la lista ordenada
    print("--- LISTA DE SUELDOS ORDENADA (de menor a mayor) ---")
    print(sueldos)

if __name__ == "__main__":
    ordenar_sueldos()
