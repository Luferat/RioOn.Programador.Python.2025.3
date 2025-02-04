'''
Exercício 02
Conversão de temperatura: solicite ao usuário que insira uma temperatura em 
Celsius, converta e exiba em Fahrenheit. 

Dica: °F = (°C x 9 ÷ 5) + 32
'''
# Solicita ao usuário que insira uma temperatura em Celsius
celsius = float(input("Insira a temperatura em Celsius: "))

# Converte a temperatura para Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Exibe a temperatura convertida
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")