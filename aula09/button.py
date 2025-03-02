import tkinter as tk


# Criando a janela principal
root = tk.Tk()
root.title("Meu aplicativo")
root.geometry("300x200")  # Define o tamanho da janela

# Criando um botão
btn = tk.Button(
    root,  # Nome da janela onde o botão será exibido
    text="Clique Aqui", # Texto do botão
    command=lambda: print("Botão clicado!") # O que fazer quando o botão é clicado
)
btn.pack(pady=20)  # Adiciona o botão à janela com espaçamento

# Iniciando o loop principal
root.mainloop()