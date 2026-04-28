import urllib.robotparser
from urllib.parse import urlparse

def read_robots_txt(start_url):
    """
    Lê robots.txt do domínio da URL inicial.
    Retorna um objeto RobotFileParser.
    """
    parsed = urlparse(start_url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    robots_url = f"{base_url}/robots.txt"

    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
        print(f"robots.txt carregado de: {robots_url}")
    except Exception as e:
        print(f"Não foi possível ler robots.txt: {e}")

    return rp

def is_allowed(url, robot_parser):
    """
    Verifica se o crawler (User-Agent 'EstudoCrawler') pode aceder à URL.
    """
    user_agent = "EstudoCrawler"
    if not robot_parser:
        return True  # Se não conseguimos ler, assumimos permitido (cautela)
    return robot_parser.can_fetch(user_agent, url)