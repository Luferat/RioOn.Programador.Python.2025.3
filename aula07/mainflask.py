# Importa a classe Flask da bilbioteca flask
from flask import Flask

# Criando um aplicativo Flask
app = Flask(__name__)


@app.route("/") # Criando a rota da página inicial do site
def home():
    return '''
    <h1>Hello, Joca!</h1>
    <p>Isso é um HTML</p>
    <a href="/contatos">Clique aqui para fazer contato</a>
    <a href="/sobre">Clique aqui para saber mais</a>
    '''


@app.route("/contatos") # Rota para a página contatos → http://localhost:5000/contatos
def contatos():
    return '<strong>Faça contato conosto!!!</strong>'


@app.route("/sobre") # Rota para a página sobre → http://localhost:5000/sobre
def sobreAgente():
    return '''
    Somos uma empresa poderosa
    <a href="/">Página inicial</a>
    '''

# Se eu estou em um servidor de desenvolvimento roda o aplicativo
# Se não, o aplicativo será rodado pelo servidor WSGL (Ex.: Apache → HTTP)
if __name__ == "__main__":
    app.run(debug=True)
