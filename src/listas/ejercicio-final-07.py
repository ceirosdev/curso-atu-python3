def encontrar_nombre_menor():
    nombres = []

    print("--- Ingreso de Nombres ---")
    # Ingresar 5 nombres y almacenarlos en la lista
    for i in range(5):
        nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
        nombres.append(nombre)

    print(f"Lista de nombres ingresados: {nombres}")

    # Encontrar el nombre menor en orden alfabético
    nombre_menor = min(nombres)

    # Mostrar el resultado
    print(f"El nombre de la persona menor en orden alfabético es: {nombre_menor}")

if __name__ == "__main__":
    encontrar_nombre_menor()
