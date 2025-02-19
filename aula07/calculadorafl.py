# Importa a classe Flask da bilbioteca flask
from flask import Flask, request

# Criando um aplicativo Flask
app = Flask(__name__)


@app.route("/")  # Criando a rota da página inicial do site
def home():
    return '''

<form action="/calcular" method="post" style="display:table; margin:auto;text-align:center">
    <h1>Calculadora</h1>
    <p><input type="number" name="num1" step="0.01" required></p>
    <p><input type="number" name="num2" step="0.01" required></p>
    <p>
        <button type="submit" name="operacao" value="+"> + </button>
        <button type="submit" name="operacao" value="-"> - </button>
        <button type="submit" name="operacao" value="*"> × </button>
        <button type="submit" name="operacao" value="/"> ÷ </button>
    </p>
</form>

    '''


@app.route('/calcular', methods=['POST'])
def calcular():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacao = request.form['operacao']

    print('------- DEBUG -----------------', num1, num2, operacao)

    if operacao == '+':
        resultado = f'{num1} + {num2} = {num1 + num2}'
    elif operacao == '-':
        resultado = f'{num1} - {num2} = {num1 - num2}'
    elif operacao == '*':
        resultado = f'{num1} × {num2} = {num1 * num2}'
    elif operacao == '/':
        resultado = f'{num1} ÷ {num2} = {num1 / num2}'
    else:
        resultado = 'Operação inválida'

    return f'''
        <div>
            <h1>Calculadora</h1>
            <h2>{resultado}</h2>
            <a href="/"> Fazer outro cálculo</a>
        </div>
    '''


# Se eu estou em um servidor de desenvolvimento roda o aplicativo
# Se não, o aplicativo será rodado pelo servidor WSGL (Ex.: Apache → HTTP)
if __name__ == "__main__":
    app.run(debug=True)
