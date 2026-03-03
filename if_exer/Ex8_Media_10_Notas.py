notas = []

for i in range(10):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)
media = sum(notas) / 10
acima_media = sum(1 for n in notas if n >= media)
print(f"Media: {media:.2f}")
print(f"Alunos com a nota acima da media media: {acima_media}")