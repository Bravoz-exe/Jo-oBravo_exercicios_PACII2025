pares = 0
impares = 0

for i in range(10):
    num = int(input(f"Numero {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Pares:", pares)
print("impares:", impares)