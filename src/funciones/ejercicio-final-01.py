"""
Desarrollar un programa con dos funciones. La primer solicite el ingreso de un 
entero y muestre el cuadrado de dicho valor. La segunda que solicite la carga de 
dos valores y muestre el producto de los mismos. LLamar desde el bloque del 
programa principal a ambas funciones.
"""

# Devuelve el cuadrado de un número entero recibido como parámetro
def cuadrado_entero(n: int) -> int:
    return n**2

# Recibe dos números enteros y devuelve su producto
def producto_dos_enteros(n1: int, n2: int) -> int:
    return n1 * n2

# Organiza las llamadas de las funciones anteriores para crear un programa
def punto_de_entrada() -> None:
    num1 = int(input("Escriba un número entero: "))
    print(f"El cuadrado de {num1} es {cuadrado_entero(n=num1)}")

    num2 = int(input("\nEscribe un segundo número entero: "))
    num3 = int(input("Escribe un tercer número entero: "))

    print(f"El cálculo de {num2} * {num3} = { \
        producto_dos_enteros(n1=num2, n2=num3)}")

if __name__ == "__main__":

    punto_de_entrada()
