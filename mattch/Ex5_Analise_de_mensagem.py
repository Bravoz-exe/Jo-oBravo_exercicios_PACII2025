def analisar_a_mensagem(msg):
    msg_lower = msg.lower()

    match msg_lower:
        case m if m in ("olá", "ola", "bom dia"):
            return "Saudaçao"
        case m if "tchau" in m or "adeus" in m:
            return "Despedida"
        case m if m.endswith("?"):
            return "Pergunta"
        case _:
            return "Mensagem generica"
print(analisar_a_mensagem("Tudo bem?"))