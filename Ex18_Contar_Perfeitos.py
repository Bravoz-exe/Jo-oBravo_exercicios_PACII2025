# Contar numeros perfeitos até N

n = int(input("Ate que o numero: "))
perfeitos = 0

for num in range(1, n + 1):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    if soma == num:
        perfeitos += 1
print("Quantidade dos perfeitos:", perfeitos)