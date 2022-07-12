#!/usr/bin/env python3
# Importa la clase Tk, y Label del módulo tkinter
from tkinter import Tk, Label

# Crea una ventana llamada root de la clase Tk
root = Tk()
# Ajusta la resolución o el tamaño de la ventana principal
root.geometry("500x500")

# Permite el cambio del tamaño de la ventana por anchura ni altura
root.resizable(True, True)

# Establece el tamaño minimo y máximo de la ventana al cambiarle el tamaño
root.minsize(50, 50)
root.maxsize(500, 500)

# Se define a la variable etiqueta como una etiqueta con el texto correspondiente
etiqueta = Label(text="Hola mundo!\nUniversidad Industrial de Santander Sede Socorro")

# Utiliza el método pack para acomodar la etiqueta en la ventana principal
etiqueta.pack()

# Establece la configuración de la etiqueta cambiando el color de fondo y la fuente
etiqueta.config(bg="#FAFAFA", font=("Arial", 14))

# Crea un bucle principal para la atención de eventos
root.mainloop()
