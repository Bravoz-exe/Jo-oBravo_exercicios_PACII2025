import json
import time
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from robots import read_robots_txt, is_allowed

def crawl(url_inicial, max_paginas):
    """
    Crawler ético que respeita robots.txt e evita duplicados.
    """
    visited = set()
    to_visit = [url_inicial]
    results = []

    # Ler robots.txt do domínio principal
    robots_allowed = read_robots_txt(url_inicial)

    while to_visit and len(visited) < max_paginas:
        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        # Verificar robots.txt
        if not is_allowed(current_url, robots_allowed):
            print(f"Bloqueado por robots.txt: {current_url}")
            continue

        print(f"Visitando: {current_url}")

        headers = {
            "User-Agent": "EstudoCrawler/1.0 (estudo@exemplo.com)"
        }

        try:
            response = requests.get(current_url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            title = soup.title.string.strip() if soup.title else "Sem título"

            # Extrair links
            links = []
            for a in soup.find_all("a", href=True):
                absolute_url = urljoin(current_url, a["href"])
                links.append(absolute_url)

                # Adicionar à fila se ainda não visitado
                if absolute_url not in visited and absolute_url not in to_visit:
                    to_visit.append(absolute_url)

            # Guardar dados
            results.append({
                "url": current_url,
                "titulo": title,
                "links": links[:10]  # limitar para exemplo
            })

            visited.add(current_url)

            # Delay ético
            time.sleep(1)

        except Exception as e:
            print(f"Erro ao aceder {current_url}: {e}")

    # Guardar resultados em JSON
    with open("resultados.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nCrawling concluído. {len(results)} páginas guardadas em resultados.json")
    return results