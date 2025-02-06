'''
Exercício 02
Conversão de temperatura: solicite ao usuário que insira uma temperatura em 
Celsius, converta e exiba em Fahrenheit. 

Dica: °F = (°C x 9 ÷ 5) + 32
'''

# Solicita ao usuário que insira uma temperatura em Celsius
celcius = float(input('Digite a temperatura em Celsius: '))

# Converte a temperatura para Fahrenheit
fahrenheit = (celcius * 9 / 5) + 32

# Exibe a temperatura convertida
print(f'A temperatura de {celcius}°C é equivalente a {fahrenheit}°F')