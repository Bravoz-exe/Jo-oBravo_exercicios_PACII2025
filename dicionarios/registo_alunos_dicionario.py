
alunos = {}

#  os dados de um aluno
nome = input("Introduz o nome do aluno: ")
idade = input("Introduz a idade do aluno: ")
curso = input("Introduz o curso do aluno: ")

# Guardar os dados no dicionário
alunos["nome"] = nome
alunos["idade"] = idade
alunos["curso"] = curso

# Mostrar os dados guardados
for chave, valor in alunos.items():
    print(f"{chave}: {valor}")