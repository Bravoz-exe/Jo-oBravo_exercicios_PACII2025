

while True:
    try:
        n = int(input("Introduza um número (1-30000): "))
        if 1 <= n <= 30000:
            break
        print("Valor fora do intervalo.")
    except ValueError:
        print("Entrada invalida.")

contador10 = 0

for num in range(n, 0, -1):
    divisores = 0
    soma_div = 0

    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1
            if i < num:
                soma_div += i

    # Primo
    if divisores == 2:
        primo_txt = "Sim"
    else:
        primo_txt = "Não"

    # Perfeito
    if soma_div == num:
        perfeito_txt = "Sim"
    else:
        perfeito_txt = "Não"

    print(f"\nNumero: {num}")
    print(f"Primo: {primo_txt}")
    print(f"Divisores: {divisores}")
    print(f"Perfeito: {perfeito_txt}")

    contador10 += 1

    if contador10 == 10:
        op = input("\nContinuar? (S/N) sim ou nao: ").upper()
        if op == "N":
            break
        contador10 = 0

print("\n fim do programa.")