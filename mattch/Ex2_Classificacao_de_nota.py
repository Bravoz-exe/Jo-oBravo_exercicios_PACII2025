def classificar_a_nota(nota):
    match nota:
        case n if n >= 90:
            return "Excelente"
        case n if 70 <= n <= 89:
            return "Bom"
        case n if 50 <= n <= 69:
            return "Suficiente"
        case _:
            return "Insuficiente"
print(classificar_a_nota(75))