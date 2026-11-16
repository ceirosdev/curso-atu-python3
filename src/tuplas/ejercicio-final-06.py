"""
Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada 
elemento una tupla con el nombre y el precio. Desarrollar las funciones
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15.
"""

# Lee y guarda los productos
def leer_producto_precio() -> list[str, float]:
    producto = []
    for i in range(1, 6):
        nombre = input(f"Nombre del producto {i}: ")
        precio = float(input(f"Precio del producto {i}: "))
        producto.append((nombre, precio))

        print("")

    return producto

# Carga y muestra los nombres de productos y precios
def cargar_producto_precio(prod: list[str, float]) -> None:
    for p in prod:
        print(f"Producto: {p[0]}, precio: {p[1]:.2f} €.")

# Carga y muestra los nombres de productos y precios con un criterio
def cargar_producto_precio_criterio(prod: list[str, float]) -> None:
    for i in range(len(prod)):
        precio = prod[i][1]
        if precio >= 10 and precio <= 15:
            print(f"Producto: {prod[i][0]}, precio: {prod[i][1]:.2f} €.")


if __name__ == "__main__":

    print("\tLeyendo los productos")
    productos = leer_producto_precio()

    print("\tCargando y mostrando los productos y sus precios")
    cargar_producto_precio(prod=productos)

    print("\n\tMuestra los productos con precios entre 10 y 15 €")
    cargar_producto_precio_criterio(prod=productos)
