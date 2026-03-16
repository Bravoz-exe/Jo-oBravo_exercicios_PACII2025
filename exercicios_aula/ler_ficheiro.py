
lista1 = []  # Nomes
lista2 = []  # Moradas
try:
    with open('dados.txt', 'r', encoding='utf-8') as f:
        for linha in f:
            nome, morada = linha.strip().split('|')
            lista1.append(nome)
            lista2.append(morada)
    print("Dados carregados!")
except:
    print("listas vazias.")
# Menu principal
while True:
    print("1 - Inserir")
    print("2 - Listar")
    print("3 - Salvar")
    print("4 - Sair")
    
    opcao = input("Opçao: ")
    
    if opcao == "1":
        nome = input("Nome: ")
        morada = input("Morada: ")
        lista1.append(nome)
        lista2.append(morada)
        print("Inserido!")
        
    elif opcao == "2":
        print("\n REGISTOS:")
        if len(lista1) == 0:
            print("Lista vazia")
        else:
            for i in range(len(lista1)):
                print(f"{i+1}. {lista1[i]} - {lista2[i]}")
                
    elif opcao == "3":
        with open('dados.txt', 'w', encoding='utf-8') as f:
            for i in range(len(lista1)):
                f.write(f"{lista1[i]}|{lista2[i]}\n")
        print("Guardado!")
        
    elif opcao == "4":
        with open('dados.txt', 'w', encoding='utf-8') as f:
            for i in range(len(lista1)):
                f.write(f"{lista1[i]}|{lista2[i]}\n")
        print("by by!")
        break