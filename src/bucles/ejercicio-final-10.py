alturas = [] # Lista para almacenar las alturas ingresadas
suma_total = 0 # Variable para acumular la suma de las alturas
altura_actual = 0 # Variable temporal para leer la entrada
num_alturas_ingresadas = 0 # Contador de cuántas alturas hemos tomado

print("Ingrese una altura. Ingrese 0 cuando haya terminado de ingresar.")

while True:
    entrada = input("Ingrese la altura (o 0 para terminar): ")

    if entrada == '0':
        break

    try:
        altura_actual = float(entrada)

        if altura_actual > 0:
            alturas.append(altura_actual)
            suma_total += altura_actual
            num_alturas_ingresadas += 1
        else:
            print("La altura debe ser un número positivo. Intente de nuevo.")

    except ValueError:
        print("Por favor, ingrese un número.")

if num_alturas_ingresadas > 0:
    promedio = suma_total / num_alturas_ingresadas
    print(f"Total de personas medidas: {num_alturas_ingresadas}")
    print(f"La altura promedio de las personas es: {promedio:.2f} unidades")
else:
    print("No se ingresaron alturas válidas. No se puede calcular el promedio.")
