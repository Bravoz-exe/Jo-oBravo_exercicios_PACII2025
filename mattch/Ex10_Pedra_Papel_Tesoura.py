def pedra_papel_ou_tesoura(j1, j2):
    j1 = j1.lower()
    j2 = j2.lower()

    match (j1, j2):
        case (a, b) if a == b:
            return "Empate"
        case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
            return "Jogador 1 venceu"
        case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
            return "Jogador 2 venceu"
        case _:
            return "Jogada invalida"
print(pedra_papel_ou_tesoura("pedra", "tesoura"))