'''
Exercício 07
Verificação de maioridade: solicite ao usuário que insira sua idade, então, 
exiba se a pessoa é maior ou menor de idade.
'''

# Solicita ao usuário que insira sua idade
idade = int(input("Insira sua idade: "))

# Verifica se a pessoa é maior ou menor de idade
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
