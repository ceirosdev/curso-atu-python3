"""
Desarrollar una aplicación que permita ingresar por teclado los nombres de 
5 artículos y sus precios. Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con 
un precio menor igual al valor ingresado.
"""

ARTICULOS = dict()

# 1. Cargar los nombres de artículos y precios
def nombre_precio() -> None:

    print("\n\tCargando los artículos y precios")

    indice = 1

    while True:

        nombre = input(f"Ingresa el nombre del artículo "
                       + f"{indice}: ").lower().strip()

        ARTICULOS[nombre] = float(input(f"Precio del artículo {nombre}: "))

        indice += 1

        continuar = input("\t¿Desea continuar? [Sí / No]: ").lower().strip()

        if continuar == "n":
            break

# 2. Imprimir los nombres y precios
def mostrar_nombres_y_precios():

    print("\n\tMostrando los artículos y precios")

    for n_articulo, p_articulo in ARTICULOS.items():
        print(f"Artículo: {n_articulo}; Precio {p_articulo:.2f} €")

# 3. Imprimir el nombre del artículo con un precio mayor
def articulo_mayor_precio():

    print("\n\tMostrando el artículo con mayor precio")

    nombre = ""
    precio = 0.0

    for n_articulo, p_articulo in ARTICULOS.items():
        if precio < p_articulo:
            nombre = n_articulo
            precio = p_articulo

    print(f"El artículo con mayor precio es: {nombre} con {precio:.2f} €")

# 4. Muestra todos los artículos con un precio menor al monto pasado
def informe_precios_menores(monto: float):

    print(f"\n\tMostrando los artículos con un precio menor que {monto:.2f} €")
    
    art_filtrados = dict()

    for n_articulo, p_articulo in ARTICULOS.items():

        if p_articulo < monto:
            art_filtrados[n_articulo] = p_articulo

    for n_articulo, p_articulo in art_filtrados.items():
            print(f"Artículo: {n_articulo}; Precio {p_articulo:.2f} €")
    

if __name__ == "__main__":
    nombre_precio()
    mostrar_nombres_y_precios()
    articulo_mayor_precio()
    informe_precios_menores(20)