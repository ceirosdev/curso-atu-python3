edades_mañana = []
print("--- Ingreso de Edades Turno Mañana (5 estudiantes) ---")
for i in range(5):
    try:
        edad = int(input(f"Ingrese la edad del estudiante Mañana N° {i + 1}: "))
        edades_mañana.append(edad)
    except ValueError:
        print("Error: Ingrese un número entero válido. Se omitirá esta edad.")

# Cálculo del promedio para el Turno Mañana
suma_mañana = sum(edades_mañana)
promedio_mañana = suma_mañana / 5

edades_tarde = []
print("\n--- Ingreso de Edades Turno Tarde (6 estudiantes) ---")
for i in range(6):
    try:
        edad = int(input(f"Ingrese la edad del estudiante Tarde N° {i + 1}: "))
        edades_tarde.append(edad)
    except ValueError:
        print("Error: Ingrese un número entero válido. Se omitirá esta edad.")

# Cálculo del promedio para el Turno Tarde
suma_tarde = sum(edades_tarde)
promedio_tarde = suma_tarde / 6

edades_noche = []
print("\n--- Ingreso de Edades Turno Noche (11 estudiantes) ---")
for i in range(11):
    try:
        edad = int(input(f"Ingrese la edad del estudiante Noche N° {i + 1}: "))
        edades_noche.append(edad)
    except ValueError:
        print("Error: Ingrese un número entero válido. Se omitirá esta edad.")

# Cálculo del promedio para el Turno Noche
suma_noche = sum(edades_noche)
promedio_noche = suma_noche / 11

print(f"Promedio Turno Mañana: {promedio_mañana:.2f}")
print(f"Promedio Turno Tarde: {promedio_tarde:.2f}")
print(f"Promedio Turno Noche: {promedio_noche:.2f}")

# Determinar cuál promedio es el mayor usando sentencias condicionales
if promedio_mañana > promedio_tarde and promedio_mañana > promedio_noche:
    print("\nEl turno de Mañana tiene el promedio de edades más alto.")
elif promedio_tarde > promedio_mañana and promedio_tarde > promedio_noche:
    print("El turno de Tarde tiene el promedio de edades más alto.")
else:
    print("El turno de Noche tiene el promedio de edades más alto, o hay un empate entre Mañana y Tarde.")
