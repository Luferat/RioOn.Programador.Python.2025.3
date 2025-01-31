nome = input("Digite seu nome: ") 
print(f"Olá, {nome}!")

'''
Explicando o código:

1) "nome" é uma variável que está sendo criada agora e recebe o valor (=) dela
da função `input()` que recebe o texto digitado por um usuário no terminal.

2) `print()` é uma função de saída que exibe textos no terminal. O "f" indica
que o texto deve ser formatado pelo Python, no caso a interpolação da variável
nome dentro das chaves {nome} deve ser processada antes de enviar a mensagem 
para o terminal.

Pesquise por `f-strings` e `interpolação` para saber mais.
'''
