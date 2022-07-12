#!/usr/bin/env python3
from tkinter import Tk, Label

incremento = 2
periodo = 50
tamaño_max = 40
tamaño = tamaño_min = 10


def modifica_tamano():
    global tamaño, incremento
    if tamaño > tamaño_max or tamaño < tamaño_min:
        incremento = -incremento
    tamaño += incremento
    etiqueta.configure(font=("Arial", str(tamaño), "bold"))
    etiqueta.after(periodo, modifica_tamano)


root = Tk()
root.geometry("400x200")
etiqueta = Label(text="¡Qué mareo!", font=("Arial", str(tamaño), "bold"))
etiqueta.pack(expand=True)
modifica_tamano()
root.mainloop()
