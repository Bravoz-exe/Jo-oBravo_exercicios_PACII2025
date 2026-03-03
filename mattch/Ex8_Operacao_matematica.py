def operacao_matematica(op, n1, n2):
    match op:
        case "soma":
            return n1 + n2
        case "subtrai":
            return n1 - n2
        case "multiplica":
            return n1 * n2
        case "divide":
            return n1 / n2 if n2 != 0 else "Erro: divisao por zero"
        case _:
            return "Operação invalida"
print(operacao_matematica("divide", 20, 4))