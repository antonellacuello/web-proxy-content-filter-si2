import re        # Importa a biblioteca de expressões regulares para manipulação de strings

def filtrar_palavras(html, palavras):
    # Controla se houve filtro para registrar no log
    filtrado = False       

    for palavra, substituta in palavras.items():
        novo_html = re.sub(               # Serve para procurar um texto e substiuir por outro
            palavra,                      # O que procurar
            substituta,                   # O que colocar no lugar
            html,                         # Onde procurar
            flags=re.IGNORECASE
        )

        # Verifica se o html mudou
        if novo_html != html:
            filtrado = True

        html = novo_html

    return html, filtrado