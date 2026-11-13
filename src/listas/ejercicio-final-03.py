# ejercicio-final-03

# 1. Definir la lista con 5 nombres
nombres = ["Ana", "Pedro", "Carlos", "María", "Sofía"]

# Inicializar el contador
conteo = 0

# 2. Iterar sobre la lista y contar los nombres que cumplen la condición
for nombre in nombres:
    # Verificar si la longitud del nombre (len(nombre)) es 5 o más
    if len(nombre) >= 5:
        conteo += 1

# Mostrar el resultado final
print(f"La lista de nombres es: {nombres}")
print(f"El número de nombres con 5 o más caracteres es: {conteo}")
