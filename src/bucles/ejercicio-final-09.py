notas = [] # Lista para almacenar las 10 notas
contador_mayores_o_iguales = 0
contador_menores = 0
numero_de_notas = 0 # Contador para saber cuántas notas hemos ingresado

while numero_de_notas < 10:
    try:
        nota = float(input(f"Ingrese la nota #{numero_de_notas + 1}: "))

        notas.append(nota)
        
        if nota >= 7:
            contador_mayores_o_iguales += 1
        else:
            contador_menores += 1

        numero_de_notas += 1

    except ValueError:
        print("Por favor, ingrese un número.")

print(f"\nTotal de notas ingresadas: {len(notas)}")
print(f"Notas mayores o iguales a 7: {contador_mayores_o_iguales}")
print(f"Notas menores a 7: {contador_menores}")
