'''
Exercício 6:
Escreva um programa que percorra os números de 1 a 50 e mostra na saída o seguinte:
 - Para múltiplos de 3, imprima "Fizz".
 - Para múltiplos de 5, imprima "Buzz".
 - Para múltiplos de 3 e 5, imprima "FizzBuzz".
 - Caso contrário, imprima o próprio número.
'''
# Solução:
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)