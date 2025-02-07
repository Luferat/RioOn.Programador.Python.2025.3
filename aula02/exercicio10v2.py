'''
Exercício 10
Calculadora simples: solicite ao usuário que insira dois números. Em seguida, 
solicite ao usuário que escolha uma das operações: +, -, x ou ÷. Realize a 
operação escolhida e exiba o resultado. 
'''

# Solicita ao usuário que insira dois números
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

# Exibe o menu de operações
print("Escolha uma operação:")
print("1) + → Soma")
print("2) - → Subtração")
print("3) x → Multiplicação")
print("4) ÷ → Divisão")

# Solicita ao usuário que escolha uma operação
operacao = int(input("Digite o número da operação desejada: "))

match operacao:
    case 1: # Soma
        resultado = f"O resultado de {num1} + {num2} é: {num1 + num2}"
    case 2: # Subtração
        resultado = f"O resultado de {num1} - {num2} é: {num1 - num2}"
    case 3: # Multiplicação
        resultado = f"O resultado de {num1} x {num2} é: {num1 * num2}"
    case 4: # Divisão
        if num2 != 0:
            resultado = f"O resultado de {num1} ÷ {num2} é: {num1 / num2}"
        else:
            resultado = "Erro: Divisão por zero não é permitida."
    case _:
        resultado = "Operação inválida."

#  Exibe resultado
print(resultado)
   