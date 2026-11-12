# Escribe: "Esta oración tiene cuatro espacios"
oracion = input('Oración 1: ').strip()

cantidad_espacios = 0

for caracter in oracion:
    if caracter == " ":
        cantidad_espacios += 1

if cantidad_espacios == 0:
    print("Escribiste corrido (sin espacios)")
else: 
    print(f"La oración tiene {cantidad_espacios} espacios")