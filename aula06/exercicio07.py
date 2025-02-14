'''
Exercício 7:
Soma dos números de uma lista: crie um programa que some todos os números de 
uma lista fornecida pelo usuário. O usuário insere os números separados por 
vírgula.
'''

list = input("Digite os números separados por vírgula: ").split(',')

soma = 0

for num in list: # Itera cada item da lista
    soma += int(num)

print(f"A soma dos números é: {soma}")
