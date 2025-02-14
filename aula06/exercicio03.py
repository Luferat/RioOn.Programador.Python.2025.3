'''
Exercício 3:
Adivinhe o número: o programa deve gerar um número aleatório entre 1 e 6 e 
pedir para o usuário adivinhar. Ele deve continuar pedindo até o usuário 
acertar.
'''

# Importa o módulo random que já vem com o Python
import random

# Gera um número aleatório entre 1 e 6 usando a função randint do módulo random
numero = random.randint(1, 6)

# God Mode
print(numero)

# Inicializa a variável de palpite
palpite = 0

# Enquanto o palpite for diferente do número gerado
while palpite != numero:

    # Pede um palpite ao usuário
    palpite = int(input("Adivinhe o número (entre 1 e 6): "))

    # Se o palpite for diferente do número gerado
    if palpite != numero:
        print("Tente novamente.")

    # Se o palpite for igual ao número gerado
    else:
        print("Parabéns! Você acertou.")
        break
