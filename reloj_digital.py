
from tkinter import *
from tkinter.ttk import *
from time import strftime

app= Tk()
app.config(width=600, height=500, background="gray",relief="groove", bd=10)
app.title("Reloj Digital")

frame_hora=Frame()
frame_hora.pack()
etiqueta_hm=Label(frame_hora, font=("Helvetica",76),text="H:M")
etiqueta_hm.grid(row=0,column=0)

etiqueta_s=Label(frame_hora, font=("Helvetica",40),text="S")
etiqueta_s.grid( row=0, column=1, sticky="n")

etiqueta_fecha=Label(font=("Helvetica", 22), text="dia d/m/aaaa")
etiqueta_fecha.pack(anchor="center")

def actualiza_reloj():
    etiqueta_hm.config(text=strftime("%H:%M"))
    etiqueta_s.config(text=strftime("%S"))
    etiqueta_fecha.config(text=strftime("%A, %d/%m/%Y"))
    etiqueta_s.after(100,actualiza_reloj)

actualiza_reloj()

app.mainloop()