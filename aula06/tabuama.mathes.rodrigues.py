import tkinter as tk
 
def exibir_tabuada():
    numero = int(entrada.get())
    tabuada = ''
    for i in range(1, 11):
        tabuada += f'{numero} x {i} = {numero * i}\n'
    resultado['text'] = tabuada
 
janela = tk.Tk()
janela.title("Tabuada")
 
label = tk.Label(janela, text="Digite um número que você quiser ver a tabuada:")
label.pack()
 
entrada = tk.Entry(janela)
entrada.pack()
 
botao = tk.Button(janela, text="Exibir Tabuada", command=exibir_tabuada)
botao.pack()
 
resultado = tk.Label(janela, text="")
resultado.pack()
 
janela.mainloop()
 