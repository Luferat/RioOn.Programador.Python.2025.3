import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


def conectar_bd():
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY, descricao TEXT, status TEXT)")
    conn.commit()
    conn.close()


def carregar_tarefas():
    lista_tarefas.delete(*lista_tarefas.get_children())
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    for row in cursor.fetchall():
        lista_tarefas.insert("", "end", values=row)
    conn.close()


def adicionar_tarefa():
    descricao = entrada_tarefa.get().strip()
    if descricao:
        conn = sqlite3.connect("tarefas.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tarefas (descricao, status) VALUES (?, ?)", (descricao, "Pendente"))
        conn.commit()
        conn.close()
        entrada_tarefa.delete(0, tk.END)
        carregar_tarefas()
    else:
        messagebox.showwarning(
            "Aviso", "Digite uma tarefa antes de adicionar!")


def remover_tarefa():
    try:
        item_selecionado = lista_tarefas.selection()[0]
        tarefa_id = lista_tarefas.item(item_selecionado, "values")[0]
        conn = sqlite3.connect("tarefas.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
        conn.commit()
        conn.close()
        lista_tarefas.delete(item_selecionado)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")


def concluir_tarefa():
    try:
        item_selecionado = lista_tarefas.selection()[0]
        tarefa_id = lista_tarefas.item(item_selecionado, "values")[0]
        conn = sqlite3.connect("tarefas.db")
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tarefas SET status = 'Concluído' WHERE id = ?", (tarefa_id,))
        conn.commit()
        conn.close()
        carregar_tarefas()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para concluir!")


root = tk.Tk()
root.title("Gerenciador de Tarefas")
root.geometry("500x400")
root.resizable(False, False)
entrada_tarefa = ttk.Entry(root, width=40)
entrada_tarefa.pack(pady=10)
frame_botoes = tk.Frame(root)
frame_botoes.pack()
btn_adicionar = ttk.Button(
    frame_botoes, text="Adicionar", command=adicionar_tarefa)
btn_adicionar.pack(side=tk.LEFT, padx=5)
btn_remover = ttk.Button(frame_botoes, text="Remover", command=remover_tarefa)
btn_remover.pack(side=tk.LEFT, padx=5)
btn_concluir = ttk.Button(
    frame_botoes, text="Concluir", command=concluir_tarefa)
btn_concluir.pack(side=tk.LEFT, padx=5)
colunas = ("ID", "Descrição", "Status")
lista_tarefas = ttk.Treeview(root, columns=colunas, show="headings")
for coluna in colunas:
    lista_tarefas.heading(coluna, text=coluna)
    lista_tarefas.column(coluna, width=150)
lista_tarefas.pack(pady=10)
conectar_bd()
carregar_tarefas()
tk.mainloop()
