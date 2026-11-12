# ejercicio-final-05

# Inicialización de contadores para cada tipo de triángulo
contador_equilatero = 0
contador_isosceles = 0
contador_escaleno = 0

# Solicitud de la cantidad de triángulos (n)
try:
    n = int(input("Ingrese la cantidad de triángulos a procesar (n): "))
except ValueError:
    print("Error: Debe ingresar un número entero para la cantidad.")
    exit()

# Procesar cada uno de los 'n' triángulos
for i in range(n):
    print(f"\n--- Triángulo N° {i + 1} ---")

    # Lectura de los tres lados del triángulo
    try:
        lado_a = float(input("Ingrese la longitud del lado A: "))
        lado_b = float(input("Ingrese la longitud del lado B: "))
        lado_c = float(input("Ingrese la longitud del lado C: "))

    except ValueError:
        print("Error: Ingrese valores numéricos válidos para los lados. Saltando este triángulo.")
        continue  # Saltar al siguiente ciclo si hay un error de entrada

    # 1. Clasificación del triángulo
    tipo = ""

    # Condición - Equilátero: Los tres lados son iguales
    if lado_a == lado_b and lado_b == lado_c:
        tipo = "Equilátero"
        contador_equilatero += 1

    # Condición - Isósceles: Exactamente dos lados son iguales
    elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
        tipo = "Isósceles"
        contador_isosceles += 1

    # Condición - Escaleno: Ningún lado es igual
    else:
        tipo = "Escaleno"
        contador_escaleno += 1

    # 2. Informar los resultados para el triángulo actual (Requisito a)
    print("\tClasificación del Triángulo:")
    print(f"   Lados ingresados: {lado_a}, {lado_b}, {lado_c}")
    print(f"   Tipo de triángulo: {tipo}")


print("\tCantidad de triángulos por tipo:")
print(f"   Equilátero: {contador_equilatero}")
print(f"   Isósceles: {contador_isosceles}")
print(f"   Escaleno: {contador_escaleno}")
