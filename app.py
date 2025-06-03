import firebirdsql
from flask import Flask, render_template
from flask import url_for, request, redirect

# bibliotecas importadas para o uso do Gemini
from flask import jsonify
from google import genai

# Configure com sua Chave de API (idealmente de uma variável de ambiente)
client = genai.Client(api_key="<digite aqui sua chave")

app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate_text():
    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({'error': 'Prompt não fornecido'}), 400

        user_prompt = data['prompt']

        # Chamar a API do Gemini
        response = client.models.generate_content(model="gemini-2.0-flash", contents=user_prompt)

        # Verifique se há blocos de segurança e como lidar com eles se necessário
        # Veja a documentação do Gemini para "safety ratings" e "blocked prompts"
        if response.prompt_feedback and response.prompt_feedback.block_reason:
            return jsonify({'error': f'Prompt bloqueado: {response.prompt_feedback.block_reason_message}'}), 400

        # Supondo que a resposta tenha um atributo 'text'
        # A estrutura exata da resposta pode variar; consulte a documentação da biblioteca.
        gemini_text_response = response.text

        return jsonify({'text': gemini_text_response})

    except Exception as e:
        print(f"Erro na API do Gemini ou no servidor: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/')
def lar():
    return render_template('index.html')


@app.route('/conteudo_selecao')
def conteudo_selecao():
    return render_template('conteudo_selecao.html')


@app.route('/conteudo_repeticao')
def conteudo_repeticao():
    return render_template('conteudo_repeticao.html')


@app.route('/conteudo_vetores_matrizes')
def conteudo_vetores_matrizes():
    return render_template('conteudo_vetores_matrizes.html')


@app.route('/conteudo_funcoes_procedimentos')
def conteudo_funcoes_procedimentos():
    return render_template('conteudo_funcoes_procedimentos.html')


@app.route('/conteudo_excecoes')
def conteudo_excecoes():
    return render_template('conteudo_excecoes.html')


@app.route('/prompt_gemini')
def prompt_gemini():
    return render_template('prompt_gemini.html')


@app.route('/dicionario')
def dicionario():

    conexao = firebirdsql.connect(host="localhost",database="C:\\Users\\acmar\\PycharmProjects\\projeto_final_ip\\DB\\DBPYTHON.FDB", user="SYSDBA", password="masterkey", port=63050, charset="ISO8859_1")

    cur = conexao.cursor()
    cur.execute("select id, termo, descricao from dicionario")
    dicionario_termos = cur.fetchall()

    cur.close()
    conexao.close()

    return render_template('dicionario.html', dicionario_termos=dicionario_termos)


@app.route('/novo_termo')
def novo_termo():
    return render_template('novo_termo.html')


@app.route('/criar_termo', methods=['POST',])
def criar_termo():

    termo = request.form['termo']
    descricao = request.form['descricao']

    conexao = firebirdsql.connect(host="localhost",database="C:\\Users\\acmar\\PycharmProjects\\projeto_final_ip\\DB\\DBPYTHON.FDB", user="SYSDBA", password="masterkey", port=63050, charset="ISO8859_1")
    cur = conexao.cursor()
    cur.execute("insert into dicionario (termo, descricao) Values ('" + termo + "', '" + descricao + "');")
    cur.execute("commit work;")

    cur.close()

    return redirect(url_for('lar'))


# Rota para realizar alterações no dicionário
@app.route('/alterar_termo/<int:termo_id>', methods=['POST', ])
def alterar_termo(termo_id):

    termo = request.form['termo']
    descricao = request.form['descricao']

    conexao = firebirdsql.connect(host="localhost",database="C:\\Users\\acmar\\PycharmProjects\\projeto_final_ip\\DB\\DBPYTHON.FDB", user="SYSDBA", password="masterkey", port=63050, charset="ISO8859_1")

    cur = conexao.cursor()
    cur.execute("update dicionario set termo = '" + termo + "', descricao = '" + descricao + "' where id = " + str(termo_id) + ";")
    cur.execute("commit work;")

    cur.close()

    return redirect(url_for('dicionario'))

# Rota para excluir um termo do dicionário
@app.route('/excluir_termo/<int:termo_id>', methods=['POST', ])
def excluir_termo(termo_id):

    conexao = firebirdsql.connect(host="localhost",database="C:\\Users\\acmar\\PycharmProjects\\projeto_final_ip\\DB\\DBPYTHON.FDB", user="SYSDBA", password="masterkey", port=63050, charset="ISO8859_1")

    cur = conexao.cursor()
    cur.execute("delete from dicionario where id = " + str(termo_id) + ";")
    cur.execute("commit work;")

    cur.close()

    return redirect(url_for('dicionario'))

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run()