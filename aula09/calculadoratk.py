import tkinter as tk
from tkinter import messagebox

def formataNumero(numero: float) -> str | int:
    """
    Formata um número, convertendo-o para inteiro se não tiver casas decimais ou 
    substituindo o ponto decimal por uma vírgula caso contrário.
    """
    if numero == int(numero):
        return int(numero)
    return str(numero).replace('.', ',')

def converterEntrada(entrada: str) -> float:
    """
    Converte a entrada do usuário para float, aceitando tanto ponto quanto vírgula
    como separador decimal.
    """
    try:
        return float(entrada.replace(',', '.'))
    except ValueError:
        raise ValueError("Entrada inválida. Insira um número válido.")

def calcular(operacao):
    try:
        num1 = converterEntrada(entry_num1.get())
        num2 = converterEntrada(entry_num2.get())
        
        if operacao == '+':
            resultado = f'{formataNumero(num1)} + {formataNumero(num2)} = {formataNumero(num1 + num2)}'
        elif operacao == '-':
            resultado = f'{formataNumero(num1)} - {formataNumero(num2)} = {formataNumero(num1 - num2)}'
        elif operacao == '*':
            resultado = f'{formataNumero(num1)} × {formataNumero(num2)} = {formataNumero(num1 * num2)}'
        elif operacao == '/':
            if num2 != 0:
                resultado = f'{formataNumero(num1)} ÷ {formataNumero(num2)} = {formataNumero(num1 / num2)}'
            else:
                resultado = 'Erro: divisão por zero'
        else:
            resultado = 'Erro: Operação inválida'
        
        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora Tkinter")
root.geometry("300x250")
root.resizable(False, False)

# Criando os widgets
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Número 1:").grid(row=0, column=0)
entry_num1 = tk.Entry(frame)
entry_num1.grid(row=0, column=1)

tk.Label(frame, text="Número 2:").grid(row=1, column=0)
entry_num2 = tk.Entry(frame)
entry_num2.grid(row=1, column=1)

# Botões de operação
frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)

for op in ['+', '-', '*', '/']:
    tk.Button(frame_botoes, text=op, width=5, command=lambda o=op: calcular(o)).pack(side=tk.LEFT, padx=5)

# Label para exibir o resultado
label_resultado = tk.Label(root, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

# Executando o loop principal
root.mainloop()
