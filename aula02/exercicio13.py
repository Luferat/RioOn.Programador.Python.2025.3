'''
Exercício 13
Aprovado ou Reprovado: receba a média de um aluno:  
 - Se for maior ou igual a 7, exiba "Aprovado". 
 - Se for entre 5 e 6.9, exiba "Recuperação". 
 - Caso contrário, exiba "Reprovado".
'''

# Solicita ao usuário que insira a média do aluno
media = float(input("Insira a média do aluno: "))

# Verifica a condição da média e exibe o resultado
if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 7:
    print("Recuperação")
else:
    print("Reprovado")