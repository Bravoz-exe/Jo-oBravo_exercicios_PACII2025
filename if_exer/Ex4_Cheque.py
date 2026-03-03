saldo = float(input("Saldo inicial: "))
cheque = float(input("Valor do cheque: "))

if cheque <= saldo:
    saldo -= cheque
    print(f"Cheque descontado, saldo agora: {saldo:.2f}")
else:
    print("O cheque não pode ser descontado")