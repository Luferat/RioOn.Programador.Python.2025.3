'''
Exercício 14
Faixa de Números Permitidos: peça um número ao usuário e verifique se ele está 
dentro do intervalo permitido (entre 10 e 20).
'''

# Solicita ao usuário que insira um número
numero = float(input("Insira um número: "))

# Verifica se o número está dentro do intervalo permitido e exibe o resultado
if numero >= 10 and numero <= 20:
    print("O número está dentro do intervalo permitido.")
else:
    print("O número está fora do intervalo permitido.")
