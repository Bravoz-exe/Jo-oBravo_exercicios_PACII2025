# Ler 10 números e dizer se são pares ou impares
for i in range(10):
    num = int(input(f"Número {i+1}: "))
    if num % 2 == 0:
        print("Par")
    else:
        print("Ímpar")