# Lectura de la cantidad de triángulos
try:
    n = int(input("Ingrese la cantidad de pares de datos (n): "))
except ValueError:
    print("Error: Debe ingresar un número entero.")
    exit()

# Inicialización del contador para la condición b)
contador_superficie_mayor_a_12 = 0


# Bucle for para procesar cada triángulo
for i in range(n):
    print(f"--- Procesando Triángulo N° {i + 1} ---")

    # Lectura de datos (base y altura)
    try:
        base = float(input(f"Ingrese la medida de la base para el triángulo {i + 1}: "))
        altura = float(input(f"Ingrese la medida de la altura para el triángulo {i + 1}: "))
    except ValueError:
        print("Error: Ingrese valores numéricos válidos. Saltando este triángulo.")
        continue

    # Cálculo de la superficie (Área = (base * altura) / 2)
    superficie = (base * altura) / 2

    # a) Informar los datos de cada triángulo
    print("\n--- Resultados del Triángulo ---")
    print(f"     Base: {base}")
    print(f"     Altura: {altura}")
    print(f"     Superficie (Área): {superficie:.2f}")

    # b) Verificar la condición de superficie > 12
    if superficie > 12:
        contador_superficie_mayor_a_12 += 1


# Informar el resultado final
print(f"\nCantidad de triángulos con superficie > 12: {contador_superficie_mayor_a_12}")
