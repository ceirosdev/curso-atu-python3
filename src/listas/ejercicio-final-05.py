def obtener_alturas():
    alturas = []
    print("Por favor, ingrese las 5 alturas de las personas (valores flotantes):")

    for i in range(5):
        while True:
            try:
                # Solicitar la entrada del usuario
                entrada = input(f"Altura de la persona {i + 1}: ")
                # Convertir la entrada a float
                altura = float(entrada)
                alturas.append(altura)
                break  # Salir del bucle 'while' si la conversión es exitosa
            except ValueError:
                # Manejar el error si el usuario ingresa algo que no es un número
                print("Error: Por favor, ingrese un valor numérico válido.")
    
    return alturas

def analizar_alturas(alturas):
    if not alturas:
        print("No hay datos para analizar.")
        return

    # Obtener el promedio
    suma_total = sum(alturas)
    promedio = suma_total / len(alturas)

    # Contar personas más altas y más bajas
    taller_contador = 0
    bajas_contador = 0

    for altura in alturas:
        if altura > promedio:
            taller_contador += 1
        elif altura < promedio:
            bajas_contador += 1

    # Imprimir los resultados
    print("--- Resultados del Análisis ---")
    print(f"Lista de alturas ingresadas: {alturas}")
    print(f"El promedio de altura es: {promedio:.2f}")
    print(f"Personas más altas que el promedio: {taller_contador}")
    print(f"Personas más bajas que el promedio: {bajas_contador}")


if __name__ == "__main__":
    # Cargar los datos
    alturas_personales = obtener_alturas()

    # Analizar y mostrar los resultados
    analizar_alturas(alturas_personales)
