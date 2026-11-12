try:
    sueldo = int(input("Ingrese el sueldo del operario: "))
    antiguedad = int(input("Ingrese los años de antigüedad: "))

    if sueldo < 500 and antiguedad >= 10:

        sueldo_pagar = sueldo * 1.20
        print(f"[Opción a] Se otorga un aumento del 20%. El sueldo a pagar es: {sueldo_pagar}")

    elif sueldo < 500 and antiguedad < 10:
        sueldo_pagar = sueldo * 1.05
        print(f"[Opción b] Se otorga un aumento del 5%. El sueldo a pagar es: {sueldo_pagar}")

    else:
        print(f"[Opción c] El sueldo es igual o superior a 500. Sueldo a pagar: {sueldo}")

except ValueError:
    print("Ingrese valores numéricos válidos.")
