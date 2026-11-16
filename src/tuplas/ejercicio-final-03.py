"""
- Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista 
con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores 
en una tupla) El programa debe tener las siguientes funciones:
1) Carga de los nombres de empleados y sus últimos tres sueldos.
2) Imprimir el monto total cobrado por cada empleado.
3) Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 
10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería 
ser similar a:
    
    ```python
    empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc. ]
    ```
"""

empleados = [
    ["juan", (2000, 3000, 4233)],
    ["ana", (3444, 1000, 5333)],
    ["Marcos", (2000, 1800, 1700)],
    ["Abraham", (3700, 4800, 5100)],
    ["Milena", (6700, 3800, 5400)],
]

def mostrar_nombre_sueldo(empleado: tuple[str, list[int, int, int]]) -> None:
    for emp in empleado:
        sueldo1, sueldo2, sueldo3 = emp[1]
        print(f"Empleado {emp[0]}, últimos tres sueldos: {sueldo1:.2f} €,"
              f" {sueldo2:.2f} €, {sueldo3:.2f} €.")


def monto_total_empleado(empleado: tuple[str, list[int, int, int]]) -> None:
    for emp in empleado:
        monto_total = sum(emp[1])
        print(f"El empleado {emp[0]} tiene un monto total de {monto_total:.2f}"
              "€.")


def empleados_ingreso_trimestral(
    monto_a_comparar: int,
    empleado: tuple[str, list[int, int, int]]
) -> None:
    for emp in empleado:
        monto_total = sum(emp[1])
        if monto_total > monto_a_comparar:
            print(f"Empleado({emp[0]}, {monto_total} €).")


if __name__ == "__main__":

    print("\tEmpleados y sus últimos sueldos")
    mostrar_nombre_sueldo(empleados)

    print("\n\tEmpleados y sus últimos sueldos acumulados")
    monto_total_empleado(empleados)

    print("\n\tEmpleados y con ingreso trimestral mayor a 10 000 €")
    empleados_ingreso_trimestral(monto_a_comparar=10_000, empleado=empleados)
