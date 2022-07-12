#!/usr/bin/env python3
# Importa la clase Tk, y Label del módulo tkinter, además de las variables TOP, RIGHT, LEFT, BOTTOM
from tkinter import Tk, Label, TOP, RIGHT, LEFT, BOTTOM

# Crea una ventana llamada root de la clase Tk
root = Tk()
# Ajusta la resolución o el tamaño de la ventana principal
root.geometry("500x500")

# Permite el cambio del tamaño de la ventana por anchura ni altura
root.resizable(True, True)

# Establece el tamaño minimo y máximo de la ventana al cambiarle el tamaño
root.minsize(50, 50)
root.maxsize(500, 500)

# Agregamos una etiqueta a la ventana principal con el texto correspondiente
etiqueta1 = Label(text="NORTE")
etiqueta2 = Label(text="OESTE")
etiqueta3 = Label(text="ESTE")
etiqueta4 = Label(text="SUR")

# Se muestra las diferentes etiquetas usando el método pack especificando el lado y el margen
etiqueta1.pack(side=TOP, pady=50)
etiqueta2.pack(side=LEFT, padx=50)
etiqueta3.pack(side=RIGHT, padx=50)
etiqueta4.pack(side=BOTTOM, pady=50)

# Crea un bucle principal para la atención de eventos
root.mainloop()
