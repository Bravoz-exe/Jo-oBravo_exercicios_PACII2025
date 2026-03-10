# Contar divisores

num = int(input("Numero: "))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        cont += 1
print("Divisores:", cont)