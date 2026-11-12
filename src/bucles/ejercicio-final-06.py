# Inicialización de contadores para cada cuadrante
contador_q1 = 0  # x > 0, y > 0
contador_q2 = 0  # x < 0, y > 0
contador_q3 = 0  # x < 0, y < 0
contador_q4 = 0  # x > 0, y < 0

# --- Paso 1: Solicitar la cantidad de puntos (n) con validación continua ---
while True:
    try:
        # Pedir la cantidad de puntos
        n = int(input("Ingrese la cantidad de puntos a procesar (n): "))
        # Si la conversión es exitosa, salimos del bucle de validación
        break
    except ValueError:
        # Si hay un error (no es un número), avisamos y el bucle se repite
        print("Error: Por favor, ingrese un número entero válido.")

# --- Paso 2: Bucle for para procesar los 'n' puntos ---
for i in range(n):
    print(f"\n--- Ingresando Punto N° {i + 1} ---")

    # Lectura de las coordenadas (x, y) con validación
    try:
        x = float(input("Ingrese la coordenada X: "))
        y = float(input("Ingrese la coordenada Y: "))
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese números.")
        continue  # Saltar al siguiente punto si la entrada es incorrecta

    # 3. Clasificación del cuadrante
    
    if x > 0 and y > 0:
        contador_q1 += 1
        print("Clasificado como Cuadrante I.")

    elif x < 0 and y > 0:
        contador_q2 += 1
        print("Clasificado como Cuadrante II.")

    elif x < 0 and y < 0:
        contador_q3 += 1
        print("Clasificado como Cuadrante III.")

    elif x > 0 and y < 0:
        contador_q4 += 1
        print("Clasificado como Cuadrante IV.")

    else:
        # Manejo de puntos sobre los ejes (x=0 o y=0)
        print("El punto se encuentra sobre un eje y no se cuenta en los cuadrantes.")


print(f"\nPuntos en el Cuadrante I (x>0, y>0): {contador_q1}")
print(f"Puntos en el Cuadrante II (x<0, y>0): {contador_q2}")
print(f"Puntos en el Cuadrante III (x<0, y<0): {contador_q3}")
print(f"Puntos en el Cuadrante IV (x>0, y<0): {contador_q4}")
