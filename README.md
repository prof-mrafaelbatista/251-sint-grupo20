# 251-sint-grupo20
Alexandre Chaves Martins

Estrutura do site

    - Home

    - Tela de abertura e apresentação do site

    - Fundamentos do Python
        Estruturas de seleção
        Estruturas de Repetição
        Vetores e Matrizes
        Funções e Procedimentos
        Tratamento de Exceções

    - Pergunte a IA
        Prompt para realização de consultas a IA Gemini

    - Glossário de termos
        Dicionário:  Tabela contendo termos e suas definições / descrições
        Adicionar Termo: Local onde o usuário pode acrescentar novos termos para consultas posteriores

    - Sobre
        Breve apresentação do desenvolvedor do site.

Tecnologias Utilizadas:

	HTML,
	CSS,
	Flask
	JavaScript
	Gemini IA - Google
	Base de Dados Firebird.

    Foram utilizadas as bibliotecas padrão do Flask: Flask, render_template, url_for, request, jsonify e
    redirect. Biblioteca de conexão com o banco de dados firebird: firebirdsql e as bibliotecas para
    utilização da inteligência artificial Gemini: genai.

Implementação da API:

    A implementação da API do Gemini foi realizada através de tutorial encontrado no site Google AI Studio.
    O tutorial pode ser encontrado na url:
    https://ai.google.dev/gemini-api/docs?hl=pt-br
    Aceso em: 30 de maio de 2025 às 01:03

Como executar a aplicação localmente

    Requisitos:
    	Python 3.13 (ou superior)
	    Firebird 4
	    Bibliotecas: firebirdsql (1.3.5), flask (3.1.0) e genai (1.16.1)

    Ajustes no código fonte:

    Fazer um clone do repositório e ajustar o caminho para o banco de dados firebird,
    bem como porta, usuário e senha de acesso ao banco. Introduzir sua chave para a
    API do Gemini. A chave para API pode ser adquirida no site:
    https://aistudio.google.com/apikey. Executar a aplicação.

    OBS: Aplicação está preparada para gerar um servidor local que estará respondendo
         na seguinte url: http://127.0.0.1:5000.

Sobre o Código

    Aplicativo desenvolvido na linguagem Python utilizando o framework Flask e Bootstrap.
    Foram também utilizados html, css, Javascript.  O site é responsivo graças ao
    Bootstrap e alguns recursos de css.

    app.py neste arquivo você vai encontrar toda a parte backend da aplicação. Neste arquivo
           você deve ajustar os dados de acesso ao banco de dados e também a sua chave de
           acesso ao Gemini;

    index.html arquivo principal do site. Tela de apresentação;

    modelo.html arquivo que serve de estrutura a todo o site. Este arquivo é responsável pelo
                cabeçalho, rodapé e menus do site.;

    prompt_gemini.html arquivo responsável pela comunicação com a API do Gemini;
    
    Os arquivos iniciados pelo prefixo conteudo_  contém instruções de como programar em Python.
    Pode ser observada também a presença da pasta static onde ficam as imagens e arquivos de estilo.

