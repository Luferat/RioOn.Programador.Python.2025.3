"""
Exercício 01
Soma de dois números: solicite ao usuário que insira dois números, em seguida, 
realize a soma dos números e exiba o resultado.
"""

# Solicita ao usuário que insira o primeiro número (inteiro)
num1 = int(input('Digite o primeiro número: '))

# Solicita ao usuário que insira o segundo número
num2 = int(input('Digite o segundo número: '))

# Realiza a soma dos dois números
soma = num1 + num2

# Exibe o resultado da soma (interpolação de strings)
print(f'A soma dos números {num1} e {num2} é: {soma}')
