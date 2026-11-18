"""
En una empresa se almacenaron los sueldos de 10 personas. Desarrollar las 
siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos
5) Mostrar todos los sueldos que están por debajo del promedio.
"""

SUELDOS: list[float] = []


def cargar_sueldos():

    print("\n\tCargando los sueldos de la empresa")

    indice = 1

    while True:

        SUELDOS.append(float(input(f"Sueldo {indice}: ")))

        indice += 1

        continuar = input("¿Desea continuar? [Sí / No]: ").lower().strip()

        if continuar == "n":
            break


def mostrar_sueldos():

    print("\n\tMostrando los sueldos de la empresa")

    indice = 1

    for sueldo in SUELDOS:
        print(f"{indice}: {sueldo:.2f}")
        indice += 1


def promedio_sueldos():

    # print("\n\tMostrando el promedio de los sueldos de la empresa")

    promedio = sum(SUELDOS) / len(SUELDOS)

    # print(f"El promedio de los sueldos es de {promedio:.2f}")

    return promedio


def sueldos_debajo_del_promedio():

    print("\n\tMostrando los sueldos de la empresa por debajo del promedio")

    promedio = promedio_sueldos()
    indice = 1

    for sueldo in SUELDOS:

        if sueldo < promedio:
            print(f"{indice}: {sueldo:.2f}")
            indice += 1


if __name__ == "__main__":
    
    cargar_sueldos()
    mostrar_sueldos()

    print("\n\tMostrando el promedio de los sueldos de la empresa")

    promedio = promedio_sueldos()

    print(f"El promedio de los sueldos es de {promedio:.2f}")

    sueldos_debajo_del_promedio()
