while True:
    try:
        numero = int(input("Escriba su número: "))
        
        if numero < 0 or numero > 999:
            raise ValueError
        else:
            if numero < 10:
                print(f"El número {numero} tiene una cifra")
            elif numero >= 10 and numero <= 99:
                print(f"El número {numero} tiene dos cifra")
            else:
                print(f"El número {numero} tiene tres cifras")
    
        opcion = input("¿Desea continuar? [Sí / No]: ").strip().lower()
        
        if opcion[0] == 's':
            continue
        else:
            break

    except ValueError:
        print(f"El número {numero} no es un entero válido de tres cifras")
