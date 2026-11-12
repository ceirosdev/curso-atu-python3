try:
    n = int(input("Ingrese la cantidad total de empleados (N): "))
except ValueError:
    print("❌ Error: Por favor, ingrese un número entero válido.")
    exit()

# Inicializar variables de control
suma_total = 0 # Para el importe total de sueldos (Requisito 3)
contador_100_a_300 = 0 # Para empleados entre $100 y $300
contador_mas_de_300 = 0 # Para empleados mayores a $300
empleados_ingresados = 0 # Contador para asegurar que se procesen N empleados

# 2. Bucle while para leer N sueldos
while empleados_ingresados < n:
    try:
        sueldo = float(input(f"Ingrese el sueldo del empleado #{empleados_ingresados + 1}: $"))

        suma_total += sueldo

        if 100 <= sueldo <= 300:
            contador_100_a_300 += 1
        elif sueldo > 300:
            contador_mas_de_300 += 1

        empleados_ingresados += 1

    except ValueError:
        print("Por favor, ingrese un valor numérico para el sueldo.")

print(f"Empleados con sueldo entre $100 y $300: {contador_100_a_300}")
print(f"Empleados con sueldo mayor a $300: {contador_mas_de_300}")

print(f"\nImporte total gastado en sueldos: ${suma_total:.2f}")
