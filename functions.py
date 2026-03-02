from textblob import TextBlob
import tkinter as tk

def analizar(entrada_texto,cuadro_ia,barra_humor,porcentaje_label): 
   frase =  entrada_texto.get()
   blob = TextBlob(frase)
   valor = blob.sentiment.polarity
   cuadro_ia.delete("1.0", tk.END)
   porcentaje = (valor + 1) * 50
   barra_humor["value"] = porcentaje 
   porcentaje_label.config(text=f"{porcentaje}%")

   if valor > 0.5:
       cuadro_ia.insert(tk.END,"IA is Euphoric")
       cuadro_ia.config(bg="orange")
   elif valor > 0:
       cuadro_ia.insert(tk.END,"IA is Peaceful/Happy")
       cuadro_ia.config(bg="green") 

   elif valor < 0:
    cuadro_ia.insert(tk.END,"IA is Bothers or Sad")   
    cuadro_ia.config(bg="blue")

def salir():
    exit()

def limpiar(cuadro_ia,barra_humor):
   cuadro_ia.delete("1.0",tk.END) 
