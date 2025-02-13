'''
Exercício 02:
Somando números: crie um programa que peça números ao usuário e some-os. 
O programa deve parar de pedir números quando o usuário digitar 0, e então 
exibir a soma total.
'''

# Solução:
# Inicializa a variável de soma
soma = 0

# Enquanto o número digitado for diferente de 0
while True:
    # Pede um número ao usuário
    n = int(input("Digite um número: "))

    # Se o número for 0
    if n == 0:
        break

    # Soma o número à variável de soma
    soma += n

# Exibe a soma total
print("A soma total é", soma)
