'''
Exercício 09
Verificação de número positivo, negativo ou zero: solicite ao usuário que 
insira um número. Verifique e exiba se o número é positivo, negativo ou é zero.
'''

# Solicita ao usuário que insira um número
numero = float(input("Insira um número: "))

# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
