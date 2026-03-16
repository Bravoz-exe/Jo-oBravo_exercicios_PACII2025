# Pedir uma palavra ao utilizador
palavra = input("digita uma palavra: ")

contador = {}

# Contar quantas vezes cada letra aparece
for letra in palavra:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1

print(contador)