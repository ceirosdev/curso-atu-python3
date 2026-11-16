"""
Confeccionar un programa con las siguientes funciones:
1) Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos 
valores
2) Una función que reciba como parámetro dos tuplas con los nombres y sueldos de 
empleados y muestre el nombre del empleado con sueldo mayor. 
En el bloque principal del programa llamar dos veces a la función de carga y 
seguidamente llamar a la función que muestra el nombre de empleado con sueldo 
mayor.
"""

# Muestra y devuelve el nombre y sueldo de un empleado
def nombre_sueldo_empleado(empleado: tuple[str, int]) -> tuple[str, int]:
    print(f"Empleado{empleado}")
    return empleado

# Muestra los datos del empleado con mayor sueldo
def nombres_sueldos_empleados(emp1: tuple[str, int], emp2: tuple[str, int]):

    # Mismo sueldo
    if emp1[1] == emp2[1]:
        print(f"{emp1[0]} y {emp2[0]} tienen el mismo sueldo de {emp1[1]} €")

    # El primero tiene mayor sueldo
    elif emp1[1] > emp2[1]:
        print(f"""
El empleado {emp1[0]} tiene el mayor sueldo de {emp1[1]} € frente a 
{emp2[0]} con {emp2[1]} €
""")

    # El segundo tiene mayor sueldo
    else:
        print(f"""
El empleado {emp2[0]} tiene el mayor sueldo de {emp2[1]} € frente a 
{emp1[0]} con {emp1[1]} €
""")


if __name__ == "__main__":

    print("\tEMPLEADOS")

    # 1. Primera llamada con tupla dirrectamente en el parámetro de la función
    nombre_sueldo_empleado(("Alex", 3000))
    
    juan = ("Juan", 3600)

    # 2. Segunda llamada con tupla almacenada en una variable pasada a la 
    # función
    nombre_sueldo_empleado(juan)

    # 3. Comparar los sueldos de los emleados
    nombres_sueldos_empleados(("Alex", 3000), juan)
