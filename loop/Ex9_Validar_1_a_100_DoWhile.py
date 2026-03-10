# Validar número entre 1 e 100
while True:
    numero = int(input("Digite um numero 1-100: "))
    if 1 <= numero <= 100:
        break
    print("Invalido!")

print("Valor valido.")