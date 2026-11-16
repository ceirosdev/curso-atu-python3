"""
Crear un diccionario en Python que defina como clave el número de documento de 
una persona y como valor un string con su nombre. Desarrollar las siguientes 
funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento.
"""

def cargar_datos_personales():
    DNI = ""
    nombre = ""
    datos_personales = dict()

    while True:
        DNI = input("Ingrese su número del DNI: ")
        nombre = input("Ingrese su nombre: ")

        datos_personales[DNI] = nombre

        detener_bucle = input(
            "\n¿Desea ingresar otra persona? [Sí / No]: ").lower()

        if detener_bucle == "n":
            break

    return datos_personales

def leer_datos_personales(datos: dict[str, str]):

    for dni, nomb  in datos.items():
        
        print(f"Nombre: {nomb}, DNI: {dni}.")

if __name__ == "__main__":

    datos_personales = cargar_datos_personales()

    leer_datos_personales(datos=datos_personales)
