'''
Exercício 11
Idade para Votar e Dirigir: solicite a idade do usuário e informe:
 - Se ele é menor de idade. 
 - Se pode votar mas não dirigir. 
 - Se pode votar e dirigir. 
'''

# Solicita ao usuário que insira sua idade
idade = int(input("Insira sua idade: "))

# Verifica a condição da idade e exibe o resultado
if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 21:
    print("Você pode votar mas não pode dirigir.")
else:
    print("Você pode votar e dirigir.")
