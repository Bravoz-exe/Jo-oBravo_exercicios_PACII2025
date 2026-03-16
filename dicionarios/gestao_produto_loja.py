# Criar dicionario vazio
produto = {}

# Adicionar informações ao produto
produto["nome"] = "Telemóvel"
produto["preço"] = 1500
produto["stock"] = 30

# Remover a chave stock
produto.pop("stock")

print(produto)