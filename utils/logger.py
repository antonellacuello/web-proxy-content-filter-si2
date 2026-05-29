from datetime import datetime

def registrar_log(url, acao):
    # append - adiciona no final do arquivo sem apagar o conteudo e se não existir o arquivo ele cria um novo    
    with open("log.txt", "a", encoding="utf-8") as log:
        log.write(
            f"{datetime.now()} | {url} | {acao}\n"
        )