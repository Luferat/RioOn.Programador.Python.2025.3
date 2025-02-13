'''
Exercício 8:
Desenhando um triângulo: peça ao usuário um número n entre 2 e 10 e desenhe um 
triângulo de asteriscos com n linhas.
'''

n = int(input("Digite um número entre 2 e 10: "))

if 2 <= n <= 10:
    for i in range(1, n + 1):
         print('*' * i)
else:
    print("Número fora do intervalo permitido.")
