 
def ordenar_alfabetico(palavras):
    
    n = len(palavras)
    for i in range(n):
        for j in range(0, n - i - 1):
            p1 = palavras[j]
            p2 = palavras[j + 1]
            for k in range(min(len(p1), len(p2))):
                if ord(p1[k]) > ord(p2[k]):
                    palavras[j], palavras[j + 1] = palavras[j + 1], palavras[j]
                    break
                elif ord(p1[k]) < ord(p2[k]):
                    break
            else:
                if len(p1) > len(p2):
                    palavras[j], palavras[j + 1] = palavras[j + 1], palavras[j]
    return palavras
 
 
# Teste
lista = ["banana", "uva", "abacaxi", "laranja"]
resultado = ordenar_alfabetico(lista)
print("Resultado:", resultado)
