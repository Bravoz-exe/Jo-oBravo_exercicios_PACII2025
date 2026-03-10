
def ler_numero(mensagem, minimo=None, maximo=None):
    while True:
        try:
            n = float(input(mensagem))
            if minimo is not None and n < minimo:
                print("Valor muito baixo.")
                continue
            if maximo is not None and n > maximo:
                print("Valor muito alto.")
                continue
            return n
        except ValueError:
            print("Entrada invalida.")


while True:
    print("\n=== MENU ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Tabuada")
    print("0 - Sair")

    op = input("Opção: ")

    # 🔹 Calculadora
    if op in {"1", "2", "3", "4"}:
        a = ler_numero("Primeiro numero: ")
        b = ler_numero("Segundo numero: ")

        if op == "1":
            print("Resultado:", a + b)
        elif op == "2":
            print("Resultado:", a - b)
        elif op == "3":
            print("Resultado:", a * b)
        elif op == "4":
            if b == 0:
                print("Divisão por zero.")
            else:
                print("Resultado:", a / b)

    # 🔹 Tabuada
    elif op == "5":
        n = int(ler_numero("Numero (1-1000): ", 1, 1000))

        contador = 0
        for i in range(1, n + 1):
            print(f"{n} x {i} = {n * i}")
            contador += 1

            if contador == 20:
                resp = input("Continuar? (S/N) sim ou nao: ").upper()
                if resp == "N":
                    break
                contador = 0

    elif op == "0":
        print("Estas a sair...")
        break
    else:
        print("Opção invaida.")