# Tabela ASCII de 20 em 20

contador = 0

for i in range(256):
    print(i, "=", chr(i))
    contador += 1

    if contador == 20:
        op = input("Continuar? S/N (sim ou nao): ").upper()
        if op == "N":
            break
        contador = 0