# Mostrar os 10 primeiros primos

contador = 0
numeros = 2
while contador < 10:
    divisores = 0
    for i in range(1, numeros + 1):
        if numeros % i == 0:
            divisores += 1
    if divisores == 2:
        print(numeros)
        contador += 1

    numeros += 1