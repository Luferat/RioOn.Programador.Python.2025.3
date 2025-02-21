# Importa a classe Flask da bilbioteca flask
from flask import Flask, request

# Criando um aplicativo Flask
app = Flask(__name__)


def formataNumero(numero: float) -> str | int:
    """
    Formata um número, convertendo-o para inteiro se não tiver casas decimais ou 
    substituindo o ponto decimal por uma vírgula caso contrário.

    Args:
        numero (float): O número a ser formatado.

    Returns:
        str | int: Retorna um inteiro se o número não tiver casas decimais ou uma string 
        com a vírgula como separador decimal caso contrário.
    """
    if numero == int(numero):
        return int(numero)
    return str(numero).replace('.', ',')


@app.route("/")  # Criando a rota da página inicial (/) do site
def home():  # Função executada quando a página inicial (/) é solicitada

    # HTML de resposta da página inicial
    return '''

        <form action="/calcular" method="post" style="display:table; margin:auto;text-align:center">
            <h1>Calculadora</h1>
            <p><input type="number" name="num1" step="0.000000000000001" required></p>
            <p><input type="number" name="num2" step="0.000000000000001" required></p>
            <p>
                <button type="submit" name="operacao" value="+"> + </button>
                <button type="submit" name="operacao" value="-"> - </button>
                <button type="submit" name="operacao" value="*"> × </button>
                <button type="submit" name="operacao" value="/"> ÷ </button>
            </p>
        </form>

    '''


# A rota '/calcular' só aceita solicitações do tipo "HTTP POST"
@app.route('/calcular', methods=['POST'])
def calcular():  # Função executada quando a rota "/calcular" é solicitada

    # Recebe os dados dos campos do formulário, formata e armazena em variáveis
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacao = request.form['operacao']

    # Apenas para debug
    print('------- DEBUG -----------------', num1, num2, operacao)

    # Realiza a operação solicitada e formata a saída com o resultado
    if operacao == '+':
        resultado = f'{formataNumero(num1)} + {formataNumero(num2)} = {formataNumero(num1 + num2)}'
    elif operacao == '-':
        resultado = f'{formataNumero(num1)} - {formataNumero(num2)} = {formataNumero(num1 - num2)}'
    elif operacao == '*':
        resultado = f'{formataNumero(num1)} × {formataNumero(num2)} = {formataNumero(num1 * num2)}'
    elif operacao == '/':
        if num2 != 0:
            resultado = f'{formataNumero(num1)} ÷ {formataNumero(num2)} = {formataNumero(num1 / num2)}'
        else:
            resultado = 'Erro: divisão por zero'
    else:
        resultado = 'Erro: Operação inválida'

    # HTML de saída da função
    return f'''
        <div style="display:table; margin:auto;text-align:center">
            <h1>Calculadora</h1>
            <h2><pre>{resultado}</pre></h2>
            <a href="/"> Fazer outro cálculo</a>
        </div>
    '''


# Roda o aplicativo se ele for chamado diretamente
if __name__ == "__main__":
    app.run(debug=True)
