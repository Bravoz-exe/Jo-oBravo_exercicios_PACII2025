 
def contar_minusculas(palavra):
    # Conta quantos caracteres estão entre 'a' e 'z'
    count = 0
    for c in palavra:
        if ord('a') <= ord(c) <= ord('z'):
            count += 1
    return count
 
def ordenar_por_minusculas(palavras):
    n = len(palavras)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if contar_minusculas(palavras[j]) > contar_minusculas(palavras[j + 1]):
                palavras[j], palavras[j + 1] = palavras[j + 1], palavras[j]
    return palavras
 
 
# Teste
lista = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]
resultado = ordenar_por_minusculas(lista)
print("Resultado:", resultado)
