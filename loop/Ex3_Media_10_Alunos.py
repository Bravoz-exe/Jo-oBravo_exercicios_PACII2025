# Media de 10 alunos

soma = 0

for i in range(10):
    nota = float(input(f"Nota do aluno {i+1}: "))
    soma += nota
media = soma / 10
print("Media:", media)