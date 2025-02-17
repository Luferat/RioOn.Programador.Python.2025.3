from flask import Flask, make_response, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Lista de usuários com login e senha
usuarios = [
    {'login': 'joca', 'senha': '123'},
    {'login': 'maria', 'senha': 'abc'},
    {'login': 'joao', 'senha': 'xyz'}
]

# Rota principal que exibe o formulário de login
@app.route('/')
def index():
    return render_template_string('''
        <form action="/login" method="post" style="display: table; margin:auto; border: 1px solid green; padding: 1rem">
            <h2>Fala login no aplicativo</h2>
            <p>
                Login: <input type="text" id="login" name="login" required>
            </p>
            <p>
                Senha: <input type="password" id="senha" name="senha" required>
            </p>
            <button type="submit">Entrar</button>
        </form>
    ''')

# Rota para processar o login
@app.route('/login', methods=['POST'])
def login():

    # Recebe os dados do formulário e remove os espaços em branco
    login = request.form['login'].strip()
    senha = request.form['senha'].strip()

    # Verifica se o login e a senha correspondem a algum usuário na lista
    for usuario in usuarios:
        if usuario['login'] == login and usuario['senha'] == senha:
            # Se o login for bem-sucedido, cria uma resposta com uma mensagem de sucesso
            response = make_response(f'''
                <div style="text-align: center; margin-top: 2rem">
                    <h2>Login bem-sucedido!</h2>
                    <p>Você já pode usar o aplicativo...</p>
                </div>
            ''')
            # Define um cookie com o nome de usuário
            response.set_cookie('username', f'{usuario["login"]}', max_age=60*60*24)
            return response

    # Se o login falhar, cria uma resposta com uma mensagem de erro
    response = make_response('''
        <div style="text-align: center; margin-top: 2rem">    
            <h2>Oooops!</h2>
            <p>Login ou senha incorretos</p>
            <a href="/">Tente novamente</a>
        </div>
    ''')
    # Remove o cookie de nome de usuário, se existir
    response.set_cookie('username', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)
