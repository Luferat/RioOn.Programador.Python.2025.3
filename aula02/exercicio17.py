'''
Exercício 17
Escreva um programa que leia três números quaisquer e imprima o maior e o 
menor. 
'''

# Solicita ao usuário que insira três números
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))

# Determina o maior número
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

# Determina o menor número
if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

# Determina o maior e o menor número usando `max()` e `min()`
# maior = max(num1, num2, num3)
# menor = min(num1, num2, num3)

# Exibe o maior e o menor número
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
