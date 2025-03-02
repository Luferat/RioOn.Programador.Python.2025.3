import tkinter as tk 
 
root = tk.Tk() 
root.title("Layout Grid") 
 
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=5, pady=5) 
entry_nome = tk.Entry(root) 
entry_nome.grid(row=0, column=1, padx=5, pady=5) 
 
tk.Label(root, text="Idade:").grid(row=1, column=0, padx=5, pady=5) 
entry_idade = tk.Entry(root) 
entry_idade.grid(row=1, column=1, padx=5, pady=5) 
 
tk.Button(root, text="Enviar").grid(row=2, column=0, columnspan=2, pady=10) 
 
root.mainloop() 