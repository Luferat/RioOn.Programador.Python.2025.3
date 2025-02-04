'''
Exercício 04
Verificação de número par ou ímpar: solicite ao usuário que insira um número 
inteiro, teste e exiba se o número é par ou ímpar.
'''

# Solicita ao usuário que insira um número inteiro
numero = int(input("Insira um número inteiro: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
