def classificar_o_produto(produto):
    match produto:
        case {"categoria": "eletronico", "preco": p} if p > 1000:
            return "Produto de luxo"
        case {"categoria": "eletronico", "preco": _}:
            return "Produto comum"
        case {"categoria": "alimento", "preco": _}:
            return "Produto alimentar"
        case _:
            return "Categoria desconhecida"
print(classificar_o_produto({"categoria": "eletronico", "preco": 1500}))  