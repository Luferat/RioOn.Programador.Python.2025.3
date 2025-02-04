'''
Exercício 15
Cadastro Simples com Regras: peça ao usuário idade e renda mensal. Se a idade 
for maior que 18 ou a renda for maior que R$ 3000, ele poderá se cadastrar. 
Caso contrário, exiba "Cadastro não permitido".
'''

# Solicita ao usuário que insira a idade
idade = int(input("Insira sua idade: "))

# Solicita ao usuário que insira a renda mensal
renda = float(input("Insira sua renda mensal: "))

# Verifica se o usuário pode se cadastrar e exibe o resultado
if idade > 18 or renda > 3000:
    print("Cadastro permitido")
else:
    print("Cadastro não permitido")
