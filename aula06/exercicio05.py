'''
Exercício 5:
Contagem progressiva: peça ao usuário um número inteiro positivo e exiba uma 
contagem de 1 até esse número usando um loop for e range. 
'''

n = int(input("Digite um número inteiro positivo: "))
# Verifica se o número é positivo
if n > 0:
    for i in range(1, n + 1):
        print(i)
else:
    print("Número inválido.")
