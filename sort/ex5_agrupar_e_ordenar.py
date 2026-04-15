 
def ordenar_grupo(grupo):
    n = len(grupo)
    for i in range(n):
        for j in range(0, n - i - 1):
            p1 = grupo[j]
            p2 = grupo[j + 1]
            for k in range(min(len(p1), len(p2))):
                if ord(p1[k]) > ord(p2[k]):
                    grupo[j], grupo[j + 1] = grupo[j + 1], grupo[j]
                    break
                elif ord(p1[k]) < ord(p2[k]):
                    break
            else:
                if len(p1) > len(p2):
                    grupo[j], grupo[j + 1] = grupo[j + 1], grupo[j]
    return grupo
 
def agrupar_e_ordenar(palavras):
    grupos = {}
 
    for palavra in palavras:
        letra = palavra[0].lower()
        if letra not in grupos:
            grupos[letra] = []
        grupos[letra].append(palavra)
 
    for letra in grupos:
        grupos[letra] = ordenar_grupo(grupos[letra])
 
    return grupos
 
 
# Teste
lista = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
resultado = agrupar_e_ordenar(lista)
print("Resultado:")
for letra, grupo in resultado.items():
    print(f"  '{letra}': {grupo}")
