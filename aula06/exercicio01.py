'''
Exercicio 01:
Contagem regressiva: escreva um programa que peça ao usuário um número inteiro 
positivo e exiba uma contagem regressiva até 1, usando um loop while.
'''

n = int(input("Digite um número inteiro positivo: "))

if n > 0:
    while n > 0:
        print(n)
        n -= 1
else:
    print("Número inválido.")
