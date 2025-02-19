# Importa as dependências da biblioteca Flask
from flask import Flask, request, jsonify
import requests

# Criando um aplicativo Flask
app = Flask(__name__)


@app.route("/")  # Rota da página inicial do site
def home():
    # Mostra página inicial no front-end
    return '''
        <form method="post" action="/logradouro" style="display: table; margin: auto; text-align: center">
            <h1>Pesquisa de CEP</h1>
            <p>Digite o CEP (somente números):</p>
            <p>
                <input type="number" name="cep" min="0" max="99999999" required>
                <button type="submit">Pesquisar</button>
            </p>
        </form>
    '''


@app.route('/logradouro', methods=['POST'])  # Rota '/logradouro'
def logradouro():

    # Recebe o CEP do formulário
    cep = request.form['cep']

    # URL da API de CEPs
    url = f"https://viacep.com.br/ws/{cep}/json/"

    # Chama a API e armazena a resposta em 'response'
    response = requests.get(url)

    # Incializa a formatação do HTML de saída
    saida = '''
        <div style="display: table; margin: auto">
            <h1 style="text-align:center">Pesquisa de CEP</h1>
    '''

    if response.status_code == 200:

        # Se o status HTTP da resposta é 200 (SUCCESS), recebe os dados em um dicionário 'data'
        data = response.json()

        if "erro" not in data:
            # Se não tem a palavra "erro" em 'data' cria uma lista não ordenada no HTML → <ul>
            saida += '<pre><ul>'

            # Loop para pegar todos os dados do dicionário e formatar como item da lista HTML → <li>
            for chave, valor in data.items():
                saida += f'<li><strong>{chave.capitalize()}:</strong> {valor}</li>'

            # Fecha a lista HTML
            saida += '</ul></pre>'

        else:
            # Se tem a mpalavra "erro", o CEP não foi encontrado
            saida += "Erro: CEP não encontrado"
    else:
        # Se o status da resposta é diferente de 200, ocorreu uma falha
        saida += "Erro: Falha na requisição"

    # Fecha as tags HTML
    saida += '''
            <p style="text-align:center"><a href="/">Fazer outra pesquisa</a></p>
        </div>
    '''

    # Envia o HTML pronto para o front-end
    return saida


# Roda o aplicativo se ele for chamado diretamente
if __name__ == "__main__":
    app.run(debug=True)
