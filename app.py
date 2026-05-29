# Flask cria a aplicação 
# render_template carrega páginas HTML 
# request permite acessar dados enviados pelo navegador, como o valor digitado no formulário
# redirect redireciona o usuário para outra rota.
from flask import Flask, render_template, request, redirect         
import requests                     # Biblioteca para fazer requisições HTTP

from urllib.parse import urlparse   # Biblioteca para analisar URLs, urlparse serve para extrair o domínio da URL

# Import das minhas funções
from utils.loader import (
    carregar_bloqueados,
    carregar_palavras
)
from utils.filters import filtrar_palavras
from utils.logger import registrar_log

# Cria a aplicação Flask e indica onde está o arquivo principal da aplicação
app = Flask(__name__)

# Rotas
# Define a rota inicial, página home
@app.route('/')
def home():
    # Valores estáticos exibidos na home para indicar o estado atual do proxy
    return render_template(
        "home.html",
        status="ONLINE",
        porta="5000",
        modo="DEBUG"
    )

# Define a rota usada pelo formulário da home para acessar o proxy
@app.route('/proxy')
def acessar_proxy():
    # Obtém a URL digitada pelo usuário e enviada para a rota /proxy
    url = request.args.get('url')
    
    # Tratamento de erros
    # Erro na escrita da URL
    if not url:
        return render_template("error.html")
    
    # Falta do protocolo
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    # Redireciona o usuário para a rota real do proxy
    return redirect("/" + url)

# Rota principal do proxy, que recebe qualquer URL e processa a requisição
@app.route('/<path:url>')
def proxy(url):         
    try:
        dominio = urlparse(url).netloc      # Extrai o domínio da URL usando urlparse
        #print(dominio)

        bloqueados = carregar_bloqueados()  # Carrega a lista de sites bloqueados

        if dominio in bloqueados:
            registrar_log(url, "bloqueado!")
            return render_template("blocked.html", site=dominio)  # Renderiza a página de bloqueio e envia o nome do site bloqueado
        
        # Faz uma requisição GET para a URL recebida
        response = requests.get(url)

        # Verifica o tipo do conteúdo retornado pela requisição!!!
        content_type = response.headers.get("Content-Type", "")

        # Filtra apenas conteúdo HTML
        if "text/html" in content_type:
            html = response.text
            palavras = carregar_palavras() # Carrega as palavras proibidas e suas substitutas

            # Aplica o filtro de palavras no HTML e verifica se alguma palavra foi mesmo substituída
            html, filtrado = filtrar_palavras(
                html,
                palavras
            )

            # Registra a ação tomada
            if filtrado:
                registrar_log(url, "filtrado!")
            else:
                registrar_log(url, "permitido!")

            return html


        # Se não for html registra como permitido e retorna o conteúdo normal 
        registrar_log(url, "permitido")

        # Retorna: os bytes do arquivo; o status HTTP e o Content-Type que informa ao navegador como interpretar o arquivo
        # Isso permite que o navegador interprete corretamente imagens, etc
        return (
            response.content, 
            response.status_code, 
            { 
                "Content-Type": content_type 
            }
        )
    
    # Se qualquer erro acontecer mostra a página de erro
    except Exception as e:          
        return render_template("error.html")

if __name__ == '__main__':
    app.run(debug=True)