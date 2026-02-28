from textblob import TextBlob
from tkinter import ttk
import tkinter as tk 
import functions

ventana = tk.Tk()
ventana.title('My window with Sentiment')
ventana.geometry("400x300")
ventana.config(bg="#2b2b2b")      


label_instruction = tk.Label(ventana, text="How do you feel:")
label_instruction.pack(pady=10)

entrada_texto = tk.Entry(ventana,width=60)
entrada_texto.pack(pady=5)

porcentaje_label = tk.Label(ventana,text="0%", bg="#2b2b2b", fg="white",font=("Arial",12,"bold"))
barra_humor = ttk.Progressbar(ventana,orient="horizontal",length=200,mode="determinate")
barra_humor.pack(pady=10)
porcentaje_label.pack(pady=10)

boton_analizar = tk.Button(ventana, text="Analizar Humor", command=lambda:functions.analizar(entrada_texto,cuadro_ia,barra_humor,porcentaje_label), bg='lightblue', fg='black')
boton_analizar.pack(pady=20)

boton_salir = tk.Button(ventana, text="Salir",command=functions.salir,bg ="cyan", fg="brown")
boton_salir.pack(pady= 25)


cuadro_ia = tk.Text(ventana, height=4, width=40)
cuadro_ia.pack()

ventana.mainloop()  
 