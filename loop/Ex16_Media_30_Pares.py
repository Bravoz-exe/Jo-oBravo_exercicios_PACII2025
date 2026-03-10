# Media de 30 números pares (1 a 50)

soma = 0
cont = 0

while cont < 30:
    num = int(input("Numero par (1-50): "))

    if 1 <= num <= 50 and num % 2 == 0:
        soma += num
        cont += 1
    else:
        print("Invalido!")

media = soma / 30
print("Media:", media)