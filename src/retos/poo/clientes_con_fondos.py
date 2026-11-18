
from retos.poo.cliente import Cliente


def clientes_con_fondos() -> list[Cliente]:

    clientes = [
        Cliente("Ana"),
        Cliente("Jorge"),
        Cliente("Carlos"),
        Cliente("María"),
    ]

    clientes[0].monto = 500.0
    clientes[1].monto = 2700.0
    clientes[2].monto = 1200.0
    clientes[3].monto = 600.0

    return clientes
