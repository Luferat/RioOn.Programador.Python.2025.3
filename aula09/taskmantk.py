import tkinter as tk 
from tkinter import messagebox 
 
# Função para adicionar uma tarefa 
def add_task(): 
    task = entry_task.get() 
    if task: 
        listbox_tasks.insert(tk.END, task) 
        entry_task.delete(0, tk.END) 
    else: 
        messagebox.showwarning("Aviso", "Digite uma tarefa antes de adicionar.") 
 
# Função para remover uma tarefa selecionada 
def remove_task(): 
    try: 
        selected_task = listbox_tasks.curselection()[0] 
        listbox_tasks.delete(selected_task) 
    except IndexError: 
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.") 
 
# Criando a janela principal 
root = tk.Tk() 
root.title("Gerenciador de Tarefas") 
root.geometry("400x300") 
 
# Entrada de nova tarefa 
entry_task = tk.Entry(root, width=40) 
entry_task.pack(pady=10) 
 
# Botões de ação 
frame_buttons = tk.Frame(root) 
frame_buttons.pack() 
 
btn_add = tk.Button(frame_buttons, text="Adicionar", command=add_task) 
btn_add.pack(side=tk.LEFT, padx=5) 
 
btn_remove = tk.Button(frame_buttons, text="Remover", command=remove_task) 
btn_remove.pack(side=tk.LEFT, padx=5) 
 
# Lista de tarefas 
listbox_tasks = tk.Listbox(root, width=50, height=10) 
listbox_tasks.pack(pady=10) 
 
# Rodando a aplicação 
root.mainloop() 