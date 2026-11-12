print("--- Selecciona tu animal favorito ---")
print("1. Perro")
print("2. Gato")
print("3. Pájaro")
print("4. Otro")

eleccion = int(input("Ingrese el número de su opción (1, 2, 3 o 4): "))

match eleccion:
    case 1:
        print("¡El perro es un animal maravilloso! Son leales y divertidos.")
    case 2:
        print("¡El gato es elegante y misterioso! Adoran dormir.")
    case 3:
        print("¡El pájaro es libre y hermoso! Su canto alegra el día.")
    case 4:
        print("¡Otro animal! Es genial que tengas una preferencia única.")
    case _:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
