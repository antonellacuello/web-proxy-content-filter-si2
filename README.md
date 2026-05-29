# 🌐 Web Proxy — SI2

Proxy HTTP desenvolvido em Python utilizando Flask e Requests para a disciplina de Sistemas de Informação II.

O projeto funciona como um proxy intermediário entre o usuário e os sites acessados, permitindo:

- bloqueio de domínios
- filtragem de palavras
- registro de logs
- exibição de páginas personalizadas
- inspeção e modificação de conteúdo HTML

---

## Tecnologias Utilizadas
### Python
Linguagem principal utilizada no desenvolvimento do proxy.

### Motivos da escolha
- sintaxe simples
- rapidez no desenvolvimento
- ótima integração com redes e HTTP
- grande quantidade de bibliotecas

---

### Flask
Framework web utilizado para criar o servidor proxy.

### Motivos da escolha
- leve e simples
- fácil manipulação de rotas
- ideal para projetos acadêmicos
- boa integração com HTML/CSS

---

### Requests
Biblioteca utilizada para realizar requisições HTTP aos sites acessados pelo proxy.

### Motivos da escolha
- API simples
- suporte a HTTP/HTTPS
- fácil acesso a:
    - headers
    - status code
    - conteúdo HTML
    - conteúdo binário

---

## Funcionalidades
### Proxy HTTP
O sistema possui uma página inicial que permite ao usuário informar a URL desejada através de um formulário.

A página inicial fica disponível em:

```txt
http://localhost:5000
```
---

### Página Inicial
O sistema possui uma página inicial personalizada contendo:

- descrição do projeto
- funcionalidades implementadas
- informações do proxy
- formulário para acesso de URLs

### Bloqueio de Sites
O proxy verifica se o domínio acessado está presente no arquivo:

```bash
blocked.json
```

Caso esteja, o acesso é bloqueado e uma página personalizada é exibida.

---

### Filtro de Palavras
O proxy analisa páginas HTML e substitui palavras proibidas utilizando expressões regulares (re.sub()).

As palavras são definidas em:

```bash
words.json
```

---

### Logs
O sistema registra:

- acessos permitidos
- acessos bloqueados
- páginas filtradas

Os registros são salvos em:

```bash
log.txt
```

---

### Tratamento de Erros
O proxy possui tratamento básico de exceções utilizando try/except, exibindo uma página personalizada em caso de falha.

---

## Estrutura do Projeto
```bash
web-proxy/
│
├── static/
│   ├── img/
│   └── style.css
│
├── templates/
│   ├── blocked.html
│   ├── error.html
│   └── home.html
│
├── utils/
│   ├── filters.py
│   ├── loader.py
│   └── logger.py
│
├── app.py
├── blocked.json
├── log.txt
├── README.md
├── requirements.txt
└── words.json
```

---

## Instalação
### 1. Clonar o repositório

```bash
git clone https://github.com/antonellacuello/web-proxy-content-filter-si2
```

### 2. Entrar na pasta

```bash
cd web-proxy
```

### 3. Criar ambiente virtual
#### Linux/Mac

```bash
python3 -m venv .venv
```

#### Windows

```bash
python -m venv .venv
```

### 4. Ativar ambiente virtual
#### Linux/Mac

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```
--- 

## Execução
Execute o servidor Flask:

```bash
python app.py
```

O proxy ficará disponível em:

```bash
http://localhost:5000
```

---

## Limitações
O projeto possui limitações relacionadas ao HTTPS.

Em muitos casos o conteúdo HTTPS ainda pode ser filtrado porque a conexão HTTPS é estabelecida pela *biblioteca requests*, e não diretamente pelo navegador.

Entretanto, em proxies HTTP reais, o navegador normalmente utiliza o *método CONNECT* para criar um túnel criptografado TLS/SSL, impedindo que o proxy visualize ou modifique o conteúdo da página.

---

## Aprendizados
Durante o desenvolvimento do projeto foram estudados conceitos relacionados a:

- protocolo HTTP
- proxies
- rotas Flask
- requisições HTTP
- headers HTTP
- manipulação de HTML
- expressões regulares
- tratamento de erros
- transferência de conteúdo binário
- funcionamento básico de proxies web

---

## Uso de Inteligência Artificial
Ferramentas de IA foram utilizadas como apoio durante:

- esclarecimento de conceitos
- entendimento de bibliotecas
- sugestões de estrutura
- explicações sobre HTTP e proxies
- desenvolvimento de textos

Todo o código foi analisado, adaptado e compreendido antes da implementação no projeto.