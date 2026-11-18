class Cliente:

    def __init__(self, nombre):
        self.nombre = nombre
        self.monto: float = 0.0

    """def depositar(self, monto):
        self.monto = self.monto+monto

    def extraer(self, monto):
        self.monto = self.monto-monto

    def retornar_monto(self):
        return self.monto"""

    def imprimir(self):
        print(f"{self.nombre} tiene depositada la suma de {self.monto:.2f} €.")
