import re

print("=" * 50)
print("PROCESSAMENTO DO FICHEIRO TXT")
print("=" * 50)

# Exercício 1: Ler o ficheiro
with open("dados.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

print("\n📌 EXERCÍCIO 1 - Conteúdo do ficheiro:")
print(conteudo)

# Exercício 2: Encontrar todos os emails
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', conteudo)
print("\n📌 EXERCÍCIO 2 - Emails encontrados:")
for email in emails:
    print(f"  • {email}")

# Exercício 3: Encontrar todos os números de telemóvel
telemoveis = re.findall(r'\d{3}[- ]?\d{3}[- ]?\d{3}', conteudo)
print("\n📌 EXERCÍCIO 3 - Telemóveis encontrados:")
for tel in telemoveis:
    print(f"  • {tel}")

# Exercício 4: Extrair apenas os nomes
nomes = re.findall(r'Nome:\s*([^,]+)', conteudo)
print("\n📌 EXERCÍCIO 4 - Nomes encontrados:")
for nome in nomes:
    print(f"  • {nome}")

# Exercício 5: Guardar dados extraídos num novo ficheiro
with open("extraidos.txt", "w", encoding="utf-8") as f:
    linhas = conteudo.strip().split("\n")
    for linha in linhas:
        nome = re.search(r'Nome:\s*([^,]+)', linha)
        email = re.search(r'([\w\.-]+@[\w\.-]+\.\w+)', linha)
        tel = re.search(r'(\d{3}[- ]?\d{3}[- ]?\d{3})', linha)
        
        if nome and email and tel:
            f.write(f"{nome.group(1)} | {email.group(1)} | {tel.group(1)}\n")

print("\n✅ Ficheiro 'extraidos.txt' criado com sucesso!")

# Exercício 6: Validar emails que terminam em .pt
emails_pt = re.findall(r'[\w\.-]+@[\w\.-]+\.pt', conteudo)
print("\n📌 EXERCÍCIO 6 - Emails .pt encontrados:")
for email in emails_pt:
    print(f"  • {email}")

print("\n" + "=" * 50)
print("Processamento TXT concluído ✅")
print("=" * 50)