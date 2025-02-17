import tkinter as tk
from tkinter import messagebox
import random

# Função para iniciar um novo jogo
def novo_jogo():
    global numero
    numero = random.randint(1, 10)
    label_mensagem.config(text="Iniciar!")
    entry_palpite.delete(0, tk.END)

# Função para verificar o palpite do usuário
def verificar_palpite():
    try:
        palpite = int(entry_palpite.get())
        if palpite < 1 or palpite > 10:
            raise ValueError("O número deve estar entre 1 e 10.")
        
        if palpite == numero:
            messagebox.showinfo("Parabéns!", "Você acertou!")
            novo_jogo()
        else:
            label_mensagem.config(text="Tente novamente.")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Cria a janela principal
root = tk.Tk()
root.title("Adivinhe o Número")

# Cria e posiciona os widgets
label_titulo = tk.Label(root, text="Adivinhe o número (entre 1 e 10)")
label_titulo.pack(pady=5)
label_mensagem = tk.Label(root, text="Iniciar")
label_mensagem.pack(pady=5)

entry_palpite = tk.Entry(root)
entry_palpite.pack(pady=5)

button_verificar = tk.Button(root, text="Verificar", command=verificar_palpite)
button_verificar.pack(pady=5)

button_novo_jogo = tk.Button(root, text="Novo Jogo", command=novo_jogo)
button_novo_jogo.pack(pady=5)

# Inicia um novo jogo
novo_jogo()

# Inicia o loop principal da interface gráfica
root.mainloop()