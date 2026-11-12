c_notas = 0
notas = []

while c_notas != 3:
    c_notas += 1
    nota = float(input(f"Ingresa la nota {c_notas}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)

if promedio >= 7:
    print(f"¡Promocionado!, su promedio es de {promedio:.2f}")
else:
    print(f"No fue aceptado, su promedio es de {promedio:.2f}")

# No Promocionado:
# Ingresa la nota 1: 6.78
# Ingresa la nota 2: 7.21
# Ingresa la nota 3: 5.25
# No fue aceptado, su promedio es de 6.41

# Promocionado:
# Ingresa la nota 1: 6.77
# Ingresa la nota 2: 5.91
# Ingresa la nota 3: 9.34
# ¡Promocionado!, su promedio es de 7.34