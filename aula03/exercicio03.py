'''
Exercicio 3:
O programa deve imprimir de 1 até o número digitado pelo usuário, mas, dessa 
vez, apenas os números pares.
'''

# Solicita ao usuário que insira um número e converte para inteiro
num = int(input('Digite um número: '))

# Loop que vai de 1 até o número digitado pelo usuário (inclusive)
for i in range(1, num + 1):
    # Verifica se o número é par
    if i % 2 == 0:
        # Imprime o número se for par
        print(i)
