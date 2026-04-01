import re
from datetime import datetime

print("=" * 50)
print("PROCESSAMENTO DO FICHEIRO REGISTOS")
print("=" * 50)

# Ler o ficheiro
with open("registos.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

linhas = conteudo.strip().split("\n")

# Exercício 7: Extrair todos os NIFs
print("\n📌 EXERCÍCIO 7 - NIFs encontrados:")
todos_nifs = []
for linha in linhas:
    nif = re.search(r'NIF:\s*(\d{9})', linha)
    if nif:
        todos_nifs.append(nif.group(1))
        print(f"  • {nif.group(1)}")

# Exercício 8: Extrair datas no formato DD/MM/AAAA
print("\n📌 EXERCÍCIO 8 - Datas encontradas:")
todas_datas = []
for linha in linhas:
    data = re.search(r'(\d{2}/\d{2}/\d{4})', linha)
    if data:
        todas_datas.append(data.group(1))
        print(f"  • {data.group(1)}")

# Exercício 9: Extrair códigos postais portugueses
print("\n📌 EXERCÍCIO 9 - Códigos postais encontrados:")
todos_cp = []
for linha in linhas:
    cp = re.search(r'(\d{4}-\d{3})', linha)
    if cp:
        todos_cp.append(cp.group(1))
        print(f"  • {cp.group(1)}")

# Exercício 10: Extrair apenas os domínios dos sites
print("\n📌 EXERCÍCIO 10 - Domínios dos sites:")
for linha in linhas:
    site = re.search(r'https?://(?:www\.)?([^/\s]+)', linha)
    if site:
        print(f"  • {site.group(1)}")

# Exercício 11: Validar se todos os NIFs começam com dígito válido (1,2,3,5,6,8)
print("\n📌 EXERCÍCIO 11 - Validar NIFs:")
nif_valido_regex = r'^[123568]\d{8}$'
nifs_validos = []
nifs_invalidos = []

for linha in linhas:
    nif = re.search(r'NIF:\s*(\d{9})', linha)
    if nif:
        if re.match(nif_valido_regex, nif.group(1)):
            nifs_validos.append(nif.group(1))
        else:
            nifs_invalidos.append(nif.group(1))

print(f"  • NIFs válidos: {nifs_validos}")
print(f"  • NIFs inválidos: {nifs_invalidos}")

# Exercício 12: Criar ficheiro resumo.txt com os dados organizados
with open("resumo.txt", "w", encoding="utf-8") as f:
    for linha in linhas:
        nome = re.search(r'Nome:\s*([^|]+)', linha)
        nif = re.search(r'NIF:\s*(\d{9})', linha)
        data = re.search(r'(\d{2}/\d{2}/\d{4})', linha)
        cp = re.search(r'(\d{4}-\d{3})', linha)
        site = re.search(r'https?://(?:www\.)?([^/\s]+)', linha)

        if nome and nif and data and cp and site:
            f.write(f"{nome.group(1).strip()} | {nif.group(1)} | {data.group(1)} | {cp.group(1)} | {site.group(1)}\n")

print("\n✅ Ficheiro 'resumo.txt' criado com sucesso!")

# Exercício 13: Encontrar registos com datas anteriores a 2025
print("\n📌 EXERCÍCIO 13 - Registos com datas anteriores a 2025:")
datas_anteriores_2025 = []

for linha in linhas:
    data_match = re.search(r'(\d{2})/(\d{2})/(\d{4})', linha)
    if data_match:
        dia, mes, ano = data_match.groups()
        data_obj = datetime(int(ano), int(mes), int(dia))
        
        if data_obj.year < 2025:
            nome = re.search(r'Nome:\s*([^|]+)', linha)
            if nome:
                print(f"  • {nome.group(1).strip()} - {data_match.group(1)}")
                datas_anteriores_2025.append(linha)

print(f"\n  Total: {len(datas_anteriores_2025)} registos anteriores a 2025")

print("\n" + "=" * 50)
print("Processamento Registos concluído ✅")
print("=" * 50)