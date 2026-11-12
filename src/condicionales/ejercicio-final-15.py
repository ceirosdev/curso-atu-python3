import datetime # Necesario para obtener la hora actual

print("\n--- MENÚ PRINCIPAL ---")
print("1. Saludar")
print("2. Decir la hora")
print("3. Salir")
print("----------------------")

opcion = input("Ingrese el número de su opción (1, 2 o 3): ")

match opcion:
    case '1':
        print("¡Hola, querido usuario!")
    case '2':
        # Mostrar la hora actual
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"La hora actual es: {hora_actual}")
    case '3':
        print("Saliendo del programa. ¡Hasta luego!")
    case _:
        print("Opción no válida. Por favor, ingrese solo 1, 2 o 3.")
