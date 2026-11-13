# ejercicio-final-09

def procesar_notas():
    nombres = []
    notas = []
    NUM_ALUMNOS = 4

    print("--- INGRESO DE DATOS ---")
    # Ingresar nombre y nota de cada alumno (dos listas paralelas)
    for i in range(NUM_ALUMNOS):
        # Ingreso del nombre
        nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
        nombres.append(nombre)

        # Ingreso de la nota (con validación de entrada numérica)
        while True:
            try:
                nota = float(input(f"Ingrese la nota de {nombre}: "))
                notas.append(nota)
                break  # Salir del bucle si la entrada es válida
            except ValueError:
                print("Error: Por favor, ingrese una nota numérica válida.")

    print("--- REPORTE DE ALUMNOS ---")

    # Realizar un listado con nombres, notas y condición
    for nombre, nota in zip(nombres, notas):
        condicion = ""
        if nota >= 8:
            condicion = "Muy Bueno"
        elif 4 <= nota <= 7:
            condicion = "Bueno"
        else: # Nota < 4
            condicion = "Insuficiente"

        print(f"Alumno: {nombre:<15} | Nota: {nota:.2f} | Condición: {condicion}")

    # Imprimir cuántos alumnos tienen la leyenda “Muy Bueno”
    muy_buenos = 0
    for nota in notas:
        if nota >= 8:
            muy_buenos += 1

    print(f"\nTotal de alumnos con la leyenda 'Muy Bueno': {muy_buenos}")

if __name__ == "__main__":
    procesar_notas()
