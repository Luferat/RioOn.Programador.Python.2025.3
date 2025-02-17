import tkinter as tk
from tkinter import messagebox

# Lista de usuários com login e senha
usuarios = [
    {'login': 'joca', 'senha': '123'},
    {'login': 'maria', 'senha': 'abc'},
    {'login': 'joao', 'senha': 'xyz'}
]

# Função para verificar o login
def verificar_login():
    login = entry_login.get().strip()
    senha = entry_senha.get().strip()

    for usuario in usuarios:
        if usuario['login'] == login and usuario['senha'] == senha:
            messagebox.showinfo("Login bem-sucedido", "Você já pode usar o aplicativo...")
            return

    messagebox.showerror("Erro de login", "Login ou senha incorretos")

# Cria a janela principal
root = tk.Tk()
root.title("Login no Aplicativo")

# Cria e posiciona os widgets
tk.Label(root, text="Login:").grid(row=0, column=0, padx=10, pady=10)
entry_login = tk.Entry(root)
entry_login.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
entry_senha = tk.Entry(root, show="*")
entry_senha.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Entrar", command=verificar_login).grid(row=2, column=0, columnspan=2, pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()