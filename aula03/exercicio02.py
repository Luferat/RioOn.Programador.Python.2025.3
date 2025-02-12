'''
Exercício 02: 
Crie um programa que imprima os números de 70 a 50. Use estrutura de repetição.
'''
i = 70
while i >= 50:
    print(i)
    i -= 1

print('---')

# Ou, usando range

for i in range(70, 49, -1):  # O último valor (49) não é incluído
    print(i)
