'''
Exercício 7:
Soma dos números de uma lista: crie um programa que some todos os números de 
uma lista fornecida pelo usuário. O usuário insere os números separados por 
vírgula.
'''

numeros = input('Digite os números separados por vírgula: ').split(',') # '1,2,3,4,5'
soma = 0
for numero in numeros:
    soma += int(numero)
print(f'A soma dos números é {soma}.')
