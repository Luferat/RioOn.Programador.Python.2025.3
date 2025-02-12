'''
Simulando um loop `do...while` em Python
'''
while True:
    value = int(input("Digite um número maior que 10: "))
    if value > 10:
        break
print("Valor aceito:", value)
