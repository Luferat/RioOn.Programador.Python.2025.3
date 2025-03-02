import tkinter as tk 
 
root = tk.Tk() 
root.title("Canvas Exemplo") 
 
canvas = tk.Canvas(root, width=300, height=200, bg="white") 
canvas.pack() 
 
# Desenhando formas 
canvas.create_line(10, 10, 200, 100, fill="blue", width=3) 
canvas.create_rectangle(50, 50, 150, 150, outline="red", width=2) 
canvas.create_oval(100, 100, 200, 200, fill="green") 
 
root.mainloop()
