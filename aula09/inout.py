import tkinter as tk


def exibir_texto():
    texto = entrada.get()
    rotulo.config(text=f"Você digitou: {texto}")


root = tk.Tk()
root.title("Entrada de Texto")
root.geometry("300x200")

entrada = tk.Entry(root)  # Caixa de entrada
entrada.pack(pady=10)

botao = tk.Button(root, text="Exibir", command=exibir_texto)
botao.pack(pady=5)

rotulo = tk.Label(root, text="Digite algo acima")  # Rótulo inicial
rotulo.pack(pady=10)

root.mainloop()
