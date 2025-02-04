'''
Exercício 03
Cálculo da área de um retângulo: solicite ao usuário que insira a largura e a 
altura do retângulo, calcule e exiba a área deste retângulo.
'''

# Solicita ao usuário que insira a largura do retângulo
largura = float(input("Insira a largura do retângulo: "))

# Solicita ao usuário que insira a altura do retângulo
altura = float(input("Insira a altura do retângulo: "))

# Calcula a área do retângulo
area = largura * altura

# Exibe a área calculada
print(f"A área do retângulo é: {area:.2f}")
