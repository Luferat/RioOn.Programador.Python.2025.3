'''
Exercício 08
Classificação de notas: solicite ao usuário que insira uma nota de 0 a 100 e 
atribua um conceito à nota, conforme o caso: 
 - 90 ou mais → Conceito A
 - 80 ou mais → Conceito B 
 - 70 ou mais → Conceito C 
 - 60 ou mais → Conceito D 
 - 50 ou mais → Conceito E 
 - Abaixo de 50 → Conceito F  
'''

# Solicita ao usuário que insira uma nota de 0 a 100
nota = int(input('Digite uma nota de 0 a 100: '))

# Atribui um conceito à nota
if nota >= 90:   # 'nota >= 90' é uma expressão booleana que retorna True ou False
    conceito = 'A'
elif nota >= 80:
    conceito = 'B'
elif nota >= 70:
    conceito = 'C'
elif nota >= 60:
    conceito = 'D'
elif nota >= 50:
    conceito = 'E'
else:
    conceito = 'F'

# Exibe o conceito atribuído
print(f'O conceito atribuído à nota {nota} é {conceito}')
