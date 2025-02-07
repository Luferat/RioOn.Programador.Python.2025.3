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

# Atribui um conceito com match-case
match nota:
    case n if 90 <= n <= 100:
        conceito = 'A'
    case n if 80 <= n < 90:
        conceito = 'B'
    case n if 70 <= n < 80:
        conceito = 'C'
    case n if 60 <= n < 70:
        conceito = 'D'
    case n if 50 <= n < 60:
        conceito = 'E'
    case _:
        conceito = 'F'

# Exibe o conceito atribuído
print(f'O conceito atribuído à nota {nota} é {conceito}')