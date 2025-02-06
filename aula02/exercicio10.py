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

# Realiza a operação escolhida e exibe o resultado
if operacao == 1:
    resultado = f"O resultado de {num1} + {num2} é: {num1 + num2}"
elif operacao == 2:
    resultado = f"O resultado de {num1} - {num2} é: {num1 - num2}"
elif operacao == 3:
    resultado = f"O resultado de {num1} x {num2} é: {num1 * num2}"
elif operacao == 4:
    if num2 != 0:
        resultado = f"O resultado de {num1} ÷ {num2} é: {num1 / num2}"
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Operação inválida."

#  Exibe resultado
print(resultado)
   