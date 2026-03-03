def tipo_de_dia(dia):
    dia = dia.lower()
    match dia:
        case "sábado" | "sabado" | "domingo":
            return "Fim de semana"
        case "segunda" | "terça" | "terca" | "quarta" | "quinta" | "sexta":
            return "Dia útil"
        case _:
            return "Dia invalido"
print(tipo_de_dia("segunda"))