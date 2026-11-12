cant_preguntas = int(input("Cantidad de preguntas: "))
cant_correctas = int(input("Contestadas correctamente: "))

porcentaje = (cant_correctas / cant_preguntas) * 100

if porcentaje >= 90:
    print(f"Nivel máximo con un {porcentaje:.2f} %")
elif porcentaje >= 75 and porcentaje < 90:
    print(f"Nivel medio con un {porcentaje:.2f} %")
elif porcentaje >= 50 and porcentaje < 75:
    print(f"Nivel regular con un {porcentaje:.2f} %")
else:
    print(f"Nivel bajo con un {porcentaje:.2f} %")
