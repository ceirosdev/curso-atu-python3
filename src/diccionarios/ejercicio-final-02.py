"""
- Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave 
sea el número de documento del alumno. Como valor almacenar una lista con 
componentes de tipo tupla donde almacenamos nombre de materia y su nota. Crear 
las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las 
materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.
"""

alumnos = {}


# Carga de los alumnos
def cargar_alumnos():
    for i in range(3):
        dni = input("Introduce el DNI del alumno: ")

        materias = []

        cantidad = int(input("¿Cuántas materias cursa? "))

        for j in range(cantidad):
            materia = input("Introduce el nombre de la materia: ")
            nota = float(input("Introduce la nota: "))

            materias.append((materia, nota))

        alumnos[dni] = materias

    print("\nAlumnos cargados correctamente.")


# Listado de todos los alumnos con sus notas
def listar_alumnos():
    for dni, materias in alumnos.items():
        print("\nDNI:", dni)

        for materia, nota in materias:
            print("Materia:", materia, "- Nota:", nota)


# Consulta de un alumno por su DNI
def consultar_alumno():
    dni = input("\nIntroduce el DNI del alumno que deseas consultar: ")

    if dni in alumnos:
        print("\nDNI:", dni)
        print("Materias y notas:")

        for materia, nota in alumnos[dni]:
            print("Materia:", materia, "- Nota:", nota)
    else:
        print("No existe ningún alumno con ese DNI.")



if __name__ == "__main__":
    cargar_alumnos()
    listar_alumnos()
    consultar_alumno()
