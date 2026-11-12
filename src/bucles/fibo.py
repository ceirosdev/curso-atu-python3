anterior = 0
siguiente = 1

limite = 13

while True:

    actual = anterior + siguiente
    siguiente = anterior
    anterior = actual

    print(actual)

    if actual == limite:
        break