from flask import Flask, make_response, redirect, request, url_for

app = Flask(__name__)

# Lista com login e senha dos usuários
usuarios = [
    {'login': 'joca', 'senha': '123'},
    {'login': 'maria', 'senha': 'abc'},
    {'login': 'joao', 'senha': 'xyz'},
]


@app.route('/')
def index():

    # Verifica se o cookie existe
    usuario = request.cookies.get('username')
    # Se não existe
    if not usuario:
        return redirect(url_for('entrar'))  # Redireciona para a rota "entrar"

    html = f"""
<!DOCTYPE html>
<html>
<body>

   <div>

        <h2>Site de Teste</h2>

   </div>

</body>
</html>
    """

    return html


@app.route('/entrar')  # Rota para fazer login
def entrar():

    html = """
<!DOCTYPE html>
<html>
<body>

    <form action="/login" method="post" style="display:table; margin:auto; border: 2px solid grey; padding: 0 1rem">

        <h2>Faça login</h2>
        <p>
            Login:
            <input type="text" name="login" required>
        </p>
        <p>
            Senha:
            <input type="password" name="senha" required>
        </p>
        <p>
            <button type="submit">Entrar</button>
        </p>

    </form>

</body>
</html>
    """

    return html


@app.route('/login', methods=['POST'])
def login():

    # Recebe os dados do formulário
    login = request.form['login'].strip()
    senha = request.form['senha'].strip()

    # Itera a coleção em busca do login e senha
    for usuario in usuarios:
        if usuario['login'] == login and usuario['senha'] == senha:

            # Login bem sucedido

            # HTML de resposta
            html = f"""
<!DOCTYPE html>
<html>
<body>
    <div style="display:table; margin:auto">
        <h2>Olá {usuario['login'].capitalize()}!</h2>
        <p>Login bem sucedido.</p>
        <p>Você já pode usar o aplicativo...</p>
        <p><a href="/">Página inicial</a></p>
    </div>
</body>
</html>
            """

            # Armazena o HTML da resposta no cache
            response = make_response(html)

            # Cria um cookie no navegador do usuário garantindo que ele está logado
            response.set_cookie(
                'username',                 # Nome do cookie
                usuario['login'],           # Valor do cookie
                max_age=60 * 60 * 24 * 10   # Tempo de vida do cookie em segundos
            )

            # Envia os dados para o front-end quando o login for "sucesso"
            return response

    # Login falhou

    # HTML avisando da falha
    html = f"""
<!DOCTYPE html>
<html>
<body>
    <div style="display:table; margin:auto">
        <h2>Oooops!</h2>
        <p>Login ou senha incorreta.</p>
        <p><a href="/entrar">Tente novamente</a></p>
    </div>
</body>
</html>
    """

    # Armazena o HTML no cache
    response = make_response(html)

    # Apaga o cookie do usuário por segurança
    response.set_cookie(
        'username',   # Nome do cookie
        '',           # Valor do cookie
        max_age=0     # Tempo de vida do cookie em segundos
    )

    # Envia os dados para o front-end quando o login "falhar"
    return response


if __name__ == '__main__':
    app.run(debug=True)
