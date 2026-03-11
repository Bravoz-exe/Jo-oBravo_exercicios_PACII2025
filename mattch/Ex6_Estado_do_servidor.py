def estado_do_servidor(info):
    match info:
        case {"stats": "ok", "tempo_de_resposta": t} if t > 200:
            return "Servidor lento"
        case {"stats": "ok", "tempo_de_resposta": _}:
            return "Servidor ativo"
        case {"stats": "erro", "tempo_de_resposta": _}:
            return "Servidor indisponivel"
        case _:
            return "Estado desconhecido"
print(estado_do_servidor({"stats": "ok", "tempo_de_resposta": 350}))