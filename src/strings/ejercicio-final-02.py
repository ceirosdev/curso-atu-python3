# Escribe: "Hay 4 vocales"
oracion = input("Escribe una oración: ").strip().lower()

contador = 0

for caracter in oracion:
    if caracter in ['a', 'e', 'i', 'o', 'u']: 
        contador += 1

if contador == 0:
    print("No tiene vocales tu oración")
else:
    print(f"Tu oración tiene {contador} vocales")