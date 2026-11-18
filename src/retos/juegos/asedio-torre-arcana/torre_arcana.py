
class Personaje:

    def __init__(self, nombre, vida, danio):
        self.nombre = nombre
        self.vida = vida
        self.danio = danio

    def atacar(self, objetivo):
        if not self.esta_vivo():
            print(f"{self.nombre} no puede atacar porque está fuera de combate.")
            return

        print(f"{self.nombre} ataca a {objetivo.nombre}.")
        objetivo.recibir_dano(self.danio)

    def recibir_dano(self, cantidad):
        self.vida = max(0, self.vida - cantidad)

        print(
            f"{self.nombre} recibe {cantidad} puntos de daño. "
            f"Vida restante: {self.vida}"
        )

    def esta_vivo(self):
        return self.vida > 0

    def mostrar_estado(self):
        print(f"\n--- Estado de {self.nombre} ---")
        print(f"Vida: {self.vida}")

# ______________________________________________________________________________

class Mago(Personaje):

    def __init__(self):
        super().__init__("Mago", 50, 8)
        self.mana = 30

    def habilidad_especial(self, objetivo):

        if not self.esta_vivo():
            print("El mago no puede utilizar habilidades porque está fuera de combate.")
            return False

        if self.mana < 15:
            print("No tienes suficiente maná para lanzar una bola de fuego.")
            return False

        self.mana -= 15

        print(f"{self.nombre} lanza una bola de fuego.")
        objetivo.recibir_dano(20)

        return True

    def mostrar_estado(self):
        super().mostrar_estado()
        print(f"Maná: {self.mana}")

# ______________________________________________________________________________

class Guerrero(Personaje):

    def __init__(self):
        super().__init__("Guerrero", 70, 12)
        self.cargas = 2

    def habilidad_especial(self, objetivo):

        if not self.esta_vivo():
            print("El guerrero no puede utilizar habilidades porque está fuera de combate.")
            return False

        if self.cargas < 1:
            print("No tienes cargas suficientes para realizar un golpe poderoso.")
            return False

        self.cargas -= 1

        print(f"{self.nombre} realiza un golpe poderoso.")
        objetivo.recibir_dano(24)

        return True

    def mostrar_estado(self):
        super().mostrar_estado()
        print(f"Cargas disponibles: {self.cargas}")

# ______________________________________________________________________________

class TorreArcana:

    def __init__(self):

        self.personajes = [
            Mago(),
            Guerrero()
        ]

        self.guardian = Personaje("Guardián de piedra", 60, 10)

        self.personaje_elegido = None

    def seleccionar_personaje(self):

        print("\n=== TORRE ARCANA ===")
        print("Selecciona tu personaje:\n")

        for indice, personaje in enumerate(self.personajes, start=1):
            print(f"{indice}. {personaje.nombre}")

        while True:

            try:
                opcion = int(input("\nElige un personaje: "))

                if opcion in (1, 2):
                    self.personaje_elegido = self.personajes[opcion - 1]
                    print(f"\nHas elegido al {self.personaje_elegido.nombre}.")
                    break

                print("Opción no válida.")

            except ValueError:
                print("Introduce un número válido.")

    def mostrar_menu(self):

        print("\n=== MENÚ DE ACCIONES ===")
        print("1. Atacar")
        print("2. Usar habilidad especial")
        print("3. Consultar estado")
        print("4. Salir")

    def jugar(self):

        self.seleccionar_personaje()

        while (
            self.personaje_elegido.esta_vivo()
            and self.guardian.esta_vivo()
        ):

            self.mostrar_menu()

            try:
                opcion = int(input("\nSelecciona una acción: "))

            except ValueError:
                print("Introduce un número válido.")
                continue

            turno_consumido = False

            if opcion == 1:

                self.personaje_elegido.atacar(self.guardian)
                turno_consumido = True

            elif opcion == 2:

                turno_consumido = self.personaje_elegido.habilidad_especial(
                    self.guardian
                )

            elif opcion == 3:

                self.personaje_elegido.mostrar_estado()
                self.guardian.mostrar_estado()

            elif opcion == 4:

                print("\nHas abandonado la prueba de la torre.")
                return

            else:

                print("Opción no válida.")

            if turno_consumido and self.guardian.esta_vivo():

                print("\n--- Turno del guardián ---")
                self.guardian.atacar(self.personaje_elegido)

        self.mostrar_resultado()

    def mostrar_resultado(self):

        print("\n=== FIN DE LA PRUEBA ===")

        self.personaje_elegido.mostrar_estado()
        self.guardian.mostrar_estado()

        if self.personaje_elegido.esta_vivo():

            print("\n¡Enhorabuena! Has superado la prueba de la Torre Arcana.")

        else:

            print("\nEl guardián te ha derrotado. No has superado la prueba.")

# ______________________________________________________________________________

if __name__ == "__main__":

    partida = TorreArcana()
    partida.jugar()
