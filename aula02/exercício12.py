'''
Exercício 12
Login Simples: simule um sistema de login simples onde é solicitado um nome de 
usuário e senha. Se o nome for "admin" e a senha for "1234", exiba "Acesso 
permitido", caso contrário, exiba "Acesso negado".
'''

# Solicita ao usuário que insira o nome de usuário
nome_usuario = input("Insira o nome de usuário: ")

# Solicita ao usuário que insira a senha
senha = input("Insira a senha: ")

# Verifica as credenciais e exibe o resultado
if nome_usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")
