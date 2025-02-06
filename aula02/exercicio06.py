'''
Exercício 06
Cálculo de custos: escreva um programa que pergunte a quantidade de km 
percorridos por um carro alugado pelo usuário, assim como a quantidade de dias 
pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro 
custa R$ 50,00 por dia e R$ 0,18 por km rodado.
'''

# Solicita ao usuário que insira a quantidade de km percorridos
km_percorridos = float(input("Insira a quantidade de km percorridos: "))

# Solicita ao usuário que insira a quantidade de dias pelos quais o carro foi alugado
dias_alugados = int(input("Insira a quantidade de dias pelos quais o carro foi alugado: "))

# Calcula o custo total
custo_total = (dias_alugados * 50) + (km_percorridos * 0.18)

# Exibe o preço a pagar
print(f"O preço a pagar é: R$ {custo_total:.2f}")
   