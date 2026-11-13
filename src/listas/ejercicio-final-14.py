def ordenar_datos_países():
    # Crear y cargar las listas paralelas
    nombres = ["España", "México", "Argentina", "Chile", "Perú"]
    # Valores de habitantes
    habitantes = [47000000, 128000000, 45000000, 19000000, 33000000]

    print("--- DATOS INICIALES ---")
    print(f"Nombres: {nombres}")
    print(f"Habitantes: {habitantes}")

    # --- ORDENAMIENTO POR NOMBRE (ALFABÉTICO) ---

    # Crear una copia de las listas para no modificar los datos originales si fuera necesario,
    # aunque aquí modificaremos la lista 'nombres' directamente.
    nombres_ordenados = sorted(nombres)
    habitantes_ordenados_por_nombre = [habitantes[i] for i in range(len(nombres_ordenados))]

    print("\n--- ORDENAMIENTO ALFABÉTICO (Por Nombre) ---")
    print(f"Nombres ordenados: {nombres_ordenados}")
    print(f"Habitantes correspondientes: {habitantes_ordenados_por_nombre}")

    # --- ORDENAMIENTO POR HABITANTES (DE MAYOR A MENOR) ---

    # Ordenar la lista de habitantes en orden descendente (mayor a menor)
    habitantes_ordenados_por_pop = sorted(habitantes, reverse=True)

    # Crear la lista de nombres correspondiente al ordenamiento por población
    nombres_ordenados_por_pop = [nombres[i] for i in range(len(habitantes_ordenados_por_pop))]

    print("\n--- ORDENAMIENTO POR HABITANTES (De Mayor a Menor) ---")
    print(f"Nombres correspondientes: {nombres_ordenados_por_pop}")
    print(f"Habitantes ordenados: {habitantes_ordenados_por_pop}")

if __name__ == "__main__":
    ordenar_datos_países()
