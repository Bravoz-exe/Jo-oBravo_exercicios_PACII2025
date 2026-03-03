def process_a_requisicao(req):
    match req:
        case {"metodo": "GET", "conteudo": _}:
            return "Requisiçao GET recebida"
        case {"metodo": "POST", "conteudo": c} if c:
            return "Requisiçao POST com dados validos"
        case {"metodo": "POST", "conteudo": ""}:
            return "Requisiçao POST sem dados"
        case _:
            return "Metodo não suportado"
print(process_a_requisicao({"metodo": "POST", "conteudo": ""}))