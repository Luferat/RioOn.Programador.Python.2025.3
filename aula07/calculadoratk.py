import tkinter as tk
from tkinter import messagebox

# Função para realizar o cálculo


def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacao = operacao_var.get()

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            resultado = num1 / num2
        else:
            resultado = 'Operação inválida'

        label_resultado.config(text=f'Resultado: {resultado}')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")
    except ZeroDivisionError as e:
        messagebox.showerror("Erro", str(e))

# Função para limpar os campos de entrada e o resultado


def limpar():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_resultado.config(text="Resultado: ")


# Cria a janela principal
root = tk.Tk()
root.title("Calculadora")

# Cria e posiciona os widgets
tk.Label(root, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

operacao_var = tk.StringVar()
operacao_var.set('+')  # Define a operação padrão

tk.Radiobutton(root, text="+", variable=operacao_var,
               value='+').grid(row=2, column=0, padx=5, pady=5)
tk.Radiobutton(root, text="-", variable=operacao_var,
               value='-').grid(row=2, column=1, padx=5, pady=5)
tk.Radiobutton(root, text="×", variable=operacao_var,
               value='*').grid(row=3, column=0, padx=5, pady=5)
tk.Radiobutton(root, text="÷", variable=operacao_var,
               value='/').grid(row=3, column=1, padx=5, pady=5)

tk.Button(root, text="Calcular", command=calcular).grid(
    row=4, column=0, padx=5, pady=5)
tk.Button(root, text="Limpar", command=limpar).grid(
    row=4, column=1, padx=5, pady=5)

label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.grid(row=5, column=0, columnspan=2, pady=5)

# Inicia o loop principal da interface gráfica
root.mainloop()
