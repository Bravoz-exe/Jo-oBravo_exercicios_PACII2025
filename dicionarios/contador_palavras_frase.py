# Pedir frase ao utilizador
frase = input("digita uma frase: ")

contador = {}

# Separar palavras
palavras = frase.split()

# Contar ocorrências
for palavra in palavras:
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1

print(contador)