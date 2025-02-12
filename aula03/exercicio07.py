'''
Exercício 7:
Escreva um programa que crie um dicionário com pelo menos 5 produtos e seus
respectivos preços. Peça ao usuário o nome de um produto. Informe o preço caso 
o produto exista no dicionário, ou diga que o produto não foi encontrado.
'''

# Solução:
produtos = {
    'arroz': 10.0,
    'feijão': 8.0,
    'macarrão': 5.0,
    'carne': 25.0,
    'frango': 15.0
}

produto = input('Digite o nome de um produto: ').lower()

if produto in produtos:
    print(f'O preço do(a) {produto} é R$ {produtos[produto]:.2f}')  
else:
    print(f'O produto {produto} não foi encontrado.')
    

