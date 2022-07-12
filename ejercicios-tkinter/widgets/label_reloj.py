#!/usr/bin/env python3
from tkinter import Tk, Label, StringVar
import time


def actualizar_hora():
    hora = time.strftime("%H:%M:%S")
    variable_control.set(hora)
    root.after(1000, actualizar_hora)


root = Tk()
root.resizable(False, False)
variable_control = StringVar()
reloj = Label(
    textvariable=variable_control,
    fg="black",
    font=("Arial", 18),
    padx=20,
    pady=20,
    bitmap="hourglass",
    compound="left",
)
reloj.pack()
actualizar_hora()
root.mainloop()
