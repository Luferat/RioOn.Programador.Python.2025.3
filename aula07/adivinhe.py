from flask import Flask, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Chave secreta para usar sessões

# Maior número que o usuário pode adivinhar
numero_maximo = 10

@app.route('/')
def index():
    # Gera um número aleatório entre 1 e numero_maximo e armazena na sessão, se ainda não existir
    if 'numero' not in session:
        session['numero'] = random.randint(1, numero_maximo)
        # Exibe o número gerado no console (para debug)
    
    print('--------------------', session['numero']) # Good mode para debug

    # Obtém a mensagem da sessão, se existir
    mensagem = session.get('mensagem') or ''

    # Renderiza o formulário HTML
    return f'''
        <form action="/adivinhar" method="post" style="display: table; margin:auto;">
            <h2>Adivinhe o número (entre 1 e {numero_maximo})</h2>
            <input type="number" name="palpite" min="1" max="{numero_maximo}" required>
            <button type="submit">Enviar</button>
            <p>{mensagem}</p>
        </form>
    '''


@app.route('/adivinhar', methods=['POST'])
def adivinhar():
    # Obtém o palpite do usuário
    palpite = int(request.form['palpite'])
    numero = session['numero']

    # Verifica se o palpite está correto
    if palpite == numero:
        session['mensagem'] = 'Parabéns! Você acertou.'
        # Remove o número da sessão para reiniciar o jogo
        session.pop('numero', None)
    else:
        session['mensagem'] = 'Tente novamente.'

    # Redireciona de volta para a página inicial
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
