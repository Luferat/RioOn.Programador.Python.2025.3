'''
Exercício 05:
Crie duas coleções e escreva no terminal a combinação das duas coleções, por 
exemplo:

    fruta = ['maçã', 'banana', 'abacate', 'uva']
    cor = ['vermelha', 'amarela', 'verde', 'roxa']

Exemplo de saída:

    Maçã é vermelha
    Banana é amarela
'''

fruta = ['maçã', 'banana', 'abacate', 'uva']
cor = ['vermelha', 'amarela', 'verde', 'roxa']

i = 0
while i < len(fruta):
    print(f"{fruta[i].capitalize()} é {cor[i]}")
    i += 1

print('---')

fruta = ['maçã', 'banana', 'abacate', 'uva', 'ovo']
cor = ['vermelha', 'amarela', 'verde', 'roxa', 'branco']
 
for i in range(len(fruta)):
    print(f"{fruta[i].capitalize()} é {cor[i]}")

print('---')

# Solução manual não recomendada

fruta = ['maçã', 'banana', 'abacate', 'uva', 'chiclete']
cor =  ['vermelha', 'amarela', 'verde', 'roxa', 'rosa']
 
print(fruta[0], cor[0])
print(fruta[1], cor[1])
print(fruta[2], cor[2])
print(fruta[3], cor[3])
print(fruta[4], cor[4])