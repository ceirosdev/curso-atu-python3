# ejercicio-final-04

# Almacenar los sueldos (valores float) de 5 operarios
sueldos = [3500.50, 4200.00, 2800.75, 5100.00, 3950.20]

# Imprimir la lista de sueldos
print("--- Lista de Sueldos ---")
print(sueldos)
print("-" * 30)

# Calculamos la suma total de todos los sueldos
suma_total = sum(sueldos)

# Calculamos la cantidad de operarios (el tamaño de la lista)
cantidad_operarios = len(sueldos)

# Calculamos el promedio
promedio = suma_total / cantidad_operarios

# Imprimir el promedio
print(f"Suma total de sueldos: {suma_total:.2f}")
print(f"Cantidad de operarios: {cantidad_operarios}")
print(f"El promedio de sueldos es: {promedio:.2f}")
