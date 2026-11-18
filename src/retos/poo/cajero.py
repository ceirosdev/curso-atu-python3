from retos.poo.cliente import Cliente


class Cajero:

    def __init__(self):
        self.clientes: list[Cliente] = []

    # Verifica si el cliente existe por su nombre y devuelve su índice
    def cliente_e_indice(self, nombre_cliente: str) -> tuple[bool, int]:

        for i, cliente in enumerate(self.clientes):
            if cliente.nombre == nombre_cliente:
                return True, i

        return False, -1

    # Realiza el depósito a la cuenta del cliente
    def depositar(self, monto, nombre_cliente):

        # No se puede ingresar valores negativos para el monto
        if monto <= 0:
            print("El importe debe ser superior a cero.")
            return

        # Dada la condición, determina si existe el cliente y el índice en el
        # que aparece en la lista
        cliente_existe, cliente_indice = self.cliente_e_indice(nombre_cliente)

        if cliente_existe:
            # Incrementa el saldo anterior con el nuevo monto
            self.clientes[cliente_indice].monto += monto
            # Utiliza el valor de saldo actual para usarla fácilmente
            saldo_actual = self.clientes[cliente_indice].monto

            print(f"Ha ingresado a su cuenta {monto:.2f} €, su saldo actual "
                  + f"es de {saldo_actual:.2f} €.")

        else:
            # El cliente no ha sido encontrado
            print(f"El cliente con el nombre {nombre_cliente} no existe.")

    # Retira saldo del cliente
    def extraer(self, monto, nombre_cliente):

        # No se puede ingresar valores negativos para el monto
        if monto <= 0:
            print("El importe debe ser superior a cero.")
            return

        # Dada la condición, determina si existe el cliente y el índice en el
        # que aparece en la lista
        cliente_existe, cliente_indice = self.cliente_e_indice(nombre_cliente)

        if cliente_existe:
            # Obtiene el saldo actual en una sola variable
            saldo_actual = self.clientes[cliente_indice].monto

            # Evita hacer retiros que dejan la cuenta en valores negativos
            if saldo_actual >= monto:

                self.clientes[cliente_indice].monto -= monto

                # Actualiza el valor del saldo actual para usarla fácilmente
                saldo_actual = self.clientes[cliente_indice].monto

                print(f"Ha retirado de su cuenta {monto} €, "
                      + f"su saldo actual es de {saldo_actual:.2f} €.")

            else:
                print(f"No puede retirar la cantidad de {monto:.2f} € porque "
                      + f"excede a su saldo actual de {saldo_actual:.2f} €.")
        else:
            print(f"El cliente con el nombre {nombre_cliente} no existe.")

    def retornar_monto(self, nombre_cliente):
        # Dada la condición, determina si existe el cliente y el índice en el
        # que aparece en la lista
        cliente_existe, cliente_indice = self.cliente_e_indice(nombre_cliente)

        if cliente_existe:
            saldo_actual = self.clientes[cliente_indice].monto

            print(f"Bienvenido {nombre_cliente}, su saldo es de "
                  + f"{saldo_actual:.2f} €.")
        else:
            print(f"El cliente con el nombre {nombre_cliente} no existe.")
