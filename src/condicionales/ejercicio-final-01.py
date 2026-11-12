numero1 = float(input("Ingresa el pimer número: "))
numero2 = float(input("Ingresa el segundo número: "))

if numero1 >= numero2:
    print(f'{numero1} + {numero2} = {(numero1 + numero2):.2f}')
else:
    print(f'{numero1} * {numero2} = {(numero1 * numero2):.2f}')
    print(f'{numero1} / {numero2} = {(numero1 / numero2):.2f}')
