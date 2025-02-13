'''
Exercício 4:
Tabuada personalizada: peça ao usuário um número e exiba sua tabuada do 1 ao 
10, usando um loop while.
'''

# Solução:
n = int(input("Digite um número: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1
        