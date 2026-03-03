def tipo_de_dado(valor):
    match valor:
        case int():
            return "Número inteiro"
        case float():
            return "Número decimal"
        case str() as s if s.isdigit():
            return "String numérica"
        case str():
            return "String de texto"
        case list():
            return "Lista"
        case _: # caso dê erro 
            return "Tipo desconhecido"
print(tipo_de_dado([10, 20, 30]))