def tipo_de_pedido(pedido):
    match pedido:
        case {"tipo": "compra", "valor": valor}:
            return f"Compra de {valor}€"
        case {"tipo": "venda", "valor": valor}:
            return f"Venda de {valor}€"
        case _:
            return "Pedido desconhecido"
print(tipo_de_pedido({"tipo": "venda", "valor": 250}))