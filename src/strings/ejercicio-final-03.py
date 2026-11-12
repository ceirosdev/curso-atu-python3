# escribe: "1234567890"
clave = input("Escribe su clave: ").strip()

cantidad_caracteres = len(clave)

if cantidad_caracteres <= 20 and cantidad_caracteres >= 10:
    print("La clave es válida")
else:
    print("La clave tiene que tener entre 10 y 20 caracteres de longitud")