from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <form action="/calcular" method="post" style="display:block;margin:auto;text-align:center;">
            <h1>Calculadora</h1>
            <p><input type="number" id="num1" name="num1" required></p>
            <p><input type="number" id="num2" name="num2" required></p>
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

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        resultado = num1 / num2
    else:
        resultado = 'Operação inválida'

    return f'''
        <div style="text-align:center;">
            <h1>Calculadora</h1>
            <h2>{resultado}</h2>
            <a href="/">Fazer outro cálculo</a>
        </div>
    '''


if __name__ == '__main__':
    app.run(debug=True)
