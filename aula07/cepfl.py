# Importa as dependências da biblioteca Flask
from flask import Flask, request, jsonify
import requests

# Criando um aplicativo Flask
app = Flask(__name__)


@app.route("/")  # Criando a rota da página inicial do site
def home():
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


@app.route('/logradouro', methods=['POST'])
def logradouro():
    cep = request.form['cep']
    url = f"https://viacep.com.br/ws/{cep}/json/"

    response = requests.get(url)

    saida = '''
        <div style="display: table; margin: auto">
            <h1 style="text-align:center">Pesquisa de CEP</h1>
    '''

    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            saida += '<pre><ul>'
            for chave, valor in data.items():
                saida += f'<li><strong>{chave.capitalize()}:</strong> {valor}</li>'
            saida += '</ul></pre>'
        else:
            saida += "Erro: CEP não encontrado"
    else:
        saida += "Erro: Falha na requisição"

    saida += '''
            <p style="text-align:center"><a href="/">Fazer outra pesquisa</a></p>
        </div>
    '''

    return saida


# Roda o aplicativo se ele for chamado diretamente
if __name__ == "__main__":
    app.run(debug=True)
