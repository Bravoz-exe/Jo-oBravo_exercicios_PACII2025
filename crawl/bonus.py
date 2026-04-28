import json
import time
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from robots import read_robots_txt, is_allowed
import matplotlib.pyplot as plt
import networkx as nx

def crawl_bonus(url_inicial, max_paginas, same_domain_only=True):
    visited = set()
    to_visit = [url_inicial]
    results = []
    domain = urlparse(url_inicial).netloc
    graph = nx.DiGraph()

    robots_allowed = read_robots_txt(url_inicial)

    while to_visit and len(visited) < max_paginas:
        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        if not is_allowed(current_url, robots_allowed):
            print(f"Bloqueado: {current_url}")
            continue

        print(f"Visitando: {current_url}")

        headers = {"User-Agent": "EstudoCrawler/1.0"}

        try:
            response = requests.get(current_url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            # Título
            title = soup.title.string.strip() if soup.title else "Sem título"

            # Links (com ou sem filtro de domínio)
            links = []
            for a in soup.find_all("a", href=True):
                absolute_url = urljoin(current_url, a["href"])
                if same_domain_only:
                    if urlparse(absolute_url).netloc == domain:
                        links.append(absolute_url)
                        if absolute_url not in visited and absolute_url not in to_visit:
                            to_visit.append(absolute_url)
                else:
                    links.append(absolute_url)
                    if absolute_url not in visited and absolute_url not in to_visit:
                        to_visit.append(absolute_url)

            # Extrair cabeçalhos e parágrafos
            headers_extract = {}
            for i in range(1, 4):
                headers_extract[f"h{i}"] = [h.get_text(strip=True) for h in soup.find_all(f"h{i}")]
            paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")][:5]

            results.append({
                "url": current_url,
                "titulo": title,
                "links": links[:10],
                "headers": headers_extract,
                "paragraphs": paragraphs
            })

            # Adicionar ao grafo
            graph.add_node(current_url, label=title[:30])
            for link in links[:10]:
                graph.add_edge(current_url, link)

            visited.add(current_url)
            time.sleep(1)

        except Exception as e:
            print(f"Erro: {e}")

    with open("resultados_bonus.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # Desenhar gráfico
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(graph, k=2, iterations=50)
    nx.draw(graph, pos, with_labels=False, node_size=500, font_size=8, arrows=True)
    labels = nx.get_node_attributes(graph, 'label')
    nx.draw_networkx_labels(graph, pos, labels, font_size=6)
    plt.title("Grafo de Navegação entre Páginas")
    plt.savefig("grafo_navegacao.png")
    plt.show()

    return results