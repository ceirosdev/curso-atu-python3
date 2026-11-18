"""
- Plantear una función que reciba un string en mayúsculas o minúsculas y retorne 
la cantidad de letras 'a' o 'A'.
"""

def filtrar_frase_por_caracter_a(frase: str) -> None:
    contador_caracter_a = 0
    
    for i in frase.lower():
        if i in ['a', 'á']:
            contador_caracter_a += 1

    print(f"La frase contiene {contador_caracter_a} letras 'a'.")

if __name__ == "__main__":

    # Contiene 4 letras 'a'
    filtrar_frase_por_caracter_a("Las clases son abstracciones")
