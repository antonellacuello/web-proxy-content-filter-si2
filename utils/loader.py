import json

def carregar_bloqueados():                    # Memórias de guerra
    with open("blocked.json", "r") as arquivo:
        dados = json.load(arquivo)

    return dados["bloqueados"]

def carregar_palavras():
    with open("words.json", "r") as arquivo:
        return json.load(arquivo)