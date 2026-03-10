# Operações até N

n = int(input("Numero: "))
contador = 0

for i in range(1, n + 1):
    _ = n + i
    _ = n - i
    _ = n * i
    _ = n / i
    contador += 4
print("Operaçoes realizadas:", contador)