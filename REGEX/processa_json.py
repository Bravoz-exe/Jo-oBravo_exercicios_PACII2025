import json
import re

# Exercício 1: Ler o ficheiro JSON
with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

print("=" * 50)
print("PROCESSAMENTO DO FICHEIRO JSON")
print("=" * 50)

# Exercício 2: Validar emails com regex
regex_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
# Exercício 4: Validar NIFs com regex (começam com 1,2,3,5,6,8)
regex_nif = r'^[123568]\d{8}$'

# Exercício 3: Extrair domínios dos sites
print("\n📌 EXERCÍCIO 3 - Domínios dos sites:")
for p in dados:
    if "site" in p:
        site = p["site"]
        # Extrair domínio (sem https:// e www.)
        dominio = re.search(r'https?://(?:www\.)?([^/]+)', site)
        if dominio:
            print(f"  • {p['nome']}: {dominio.group(1)}")
    else:
        print(f"  • {p['nome']}: (sem site no ficheiro)")

# Exercício 5: Guardar apenas registos válidos
validos = []
print("\n📌 EXERCÍCIO 5 - Validando registos...")

for p in dados:
    # Limpar telemóvel (remover traços e espaços)
    tel = re.sub(r'[- ]', '', p["telemovel"])
    
    email_valido = re.match(regex_email, p["email"]) is not None
    nif_valido = re.match(regex_nif, p["nif"]) is not None
    tel_valido = len(tel) == 9 and tel.isdigit()
    
    print(f"  • {p['nome']}: Email: {email_valido}, NIF: {nif_valido}, Tel: {tel_valido}")
    
    if email_valido and nif_valido and tel_valido:
        validos.append(p)

# Guardar registos válidos em JSON
with open("validos.json", "w", encoding="utf-8") as f:
    json.dump(validos, f, indent=4, ensure_ascii=False)

print(f"\n✅ Guardados {len(validos)} registos válidos em 'validos.json'")

# Exercício 6: Criar ficheiro .txt com nome e email
with open("nomes_emails.txt", "w", encoding="utf-8") as f:
    for p in dados:
        f.write(f"{p['nome']} | {p['email']}\n")

print("✅ Ficheiro 'nomes_emails.txt' criado com sucesso!")
print("\n" + "=" * 50)
print("Processamento JSON concluído ✅")
print("=" * 50)