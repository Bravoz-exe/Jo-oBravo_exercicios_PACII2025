# Verificar se é primo
num = int(input("Numero: "))
divisores = 0

for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1
if divisores == 2:
    print("É primo")
else:
    print("Não é primo")