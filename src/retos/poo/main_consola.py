
from retos.poo.cajero import Cajero
from retos.poo.clientes_con_fondos import clientes_con_fondos

def solicitar_monto() -> float | None:

    try:
        return float(input("Introduce el importe: "))

    except ValueError:
        print("Error: debes introducir una cantidad numérica.")
        return None


def menu():

    cajero = Cajero()
    cajero.clientes = clientes_con_fondos()

    while True:

        print("\n========== CAJERO AUTOMÁTICO ==========")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Consultar saldo")
        print("4. Mostrar clientes")
        print("0. Salir")
        print("=======================================")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":

            nombre = input("Introduce el nombre del cliente: ")
            monto = solicitar_monto()

            if monto is not None:
                cajero.depositar(monto, nombre)

        elif opcion == "2":

            nombre = input("Introduce el nombre del cliente: ")
            monto = solicitar_monto()

            if monto is not None:
                cajero.extraer(monto, nombre)

        elif opcion == "3":

            nombre = input("Introduce el nombre del cliente: ")

            cajero.retornar_monto(nombre)

        elif opcion == "4":

            print("\n========== LISTADO DE CLIENTES ==========")

            for cliente in cajero.clientes:
                cliente.imprimir()

            print("=========================================")

        elif opcion == "0":

            print("Gracias por utilizar nuestro cajero.")
            break

        else:
            print("Opción incorrecta. Inténtalo nuevamente.")


if __name__ == "__main__":
    menu()
