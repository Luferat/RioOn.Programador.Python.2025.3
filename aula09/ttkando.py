import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Exemplo com ttk")

# Criando um botão normal (tk) e um estilizado (ttk)
btn1 = tk.Button(root, text="Botão Tkinter")
btn1.pack(pady=10)

btn2 = ttk.Button(root, text="Botão ttk")
btn2.pack(pady=10)

root.mainloop()
