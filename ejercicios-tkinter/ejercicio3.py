#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox

titulo = "Suma enteros"


def calcular_suma():
    messagebox.showinfo(titulo, "El resultado se mostrará...")
    valor_x = int(x_input.get())
    valor_y = int(y_input.get())
    resultado = valor_x + valor_y
    texto_resultados.configure(state="normal")
    texto_resultados.insert(
        tk.END, str(valor_x) + " + " + str(valor_y) + " = " + str(resultado) + "\n"
    )
    texto_resultados.configure(state="disabled")


def borrar_texto():
    messagebox.showinfo(titulo, "Todas las entradas se borrarán...")
    x_input.delete(0, tk.END)
    y_input.delete(0, tk.END)


def salir_ventana():
    messagebox.showinfo(titulo, "El programa se cerrará...")
    ventana_principal.destroy()


ventana_principal = tk.Tk()
ventana_principal.title(titulo)
ventana_principal.geometry("500x410")
ventana_principal.resizable(False, False)
ventana_principal.config(background="white")
ventana_principal.iconphoto(True, tk.PhotoImage(file="logo.png"))

frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(background="#64b446", width=480, height=180)
frame_entrada.place(x=10, y=10)

titulo = tk.Label(frame_entrada, text="SUMA DE ENTEROS")
titulo.config(background="#64b446", foreground="black", font=("Verdana", 16, "bold"))
titulo.place(x=123, y=10)

logo = tk.PhotoImage(file="uis.png")
logo_label = tk.Label(
    frame_entrada, background="white", image=logo, borderwidth=5, relief="raised"
)
logo_label.place(x=10, y=60)

x_label = tk.Label(frame_entrada, text="X =")
x_label.config(background="#64b446", foreground="black", font=("Serif", 14))
x_label.place(x=240, y=80)

x_input = tk.Entry(frame_entrada)
x_input.config(font=("Arial", 12), highlightthickness=2)
x_input.focus_set()
x_input.place(x=280, y=80)

y_label = tk.Label(frame_entrada, text="Y =")
y_label.config(background="#64b446", foreground="black", font=("Serif", 14))
y_label.place(x=240, y=120)

y_input = tk.Entry(frame_entrada)
y_input.config(font=("Arial", 12), highlightthickness=2)
y_input.place(x=280, y=120)

frame_operaciones = tk.Frame(ventana_principal)
frame_operaciones.config(background="#64b446", width=480, height=80)
frame_operaciones.place(x=10, y=200)

boton_calcular = tk.Button(
    frame_operaciones,
    text="Calcular",
    background="white",
    highlightthickness=3,
    borderwidth=2,
    bd=2,
    command=calcular_suma,
)
boton_calcular.place(x=60, y=25)

boton_borrar = tk.Button(
    frame_operaciones,
    text="Borrar",
    background="white",
    highlightthickness=3,
    borderwidth=2,
    bd=2,
    command=borrar_texto,
)
boton_borrar.place(x=205, y=25)

boton_salir = tk.Button(
    frame_operaciones,
    text="Salir",
    background="white",
    highlightthickness=3,
    borderwidth=2,
    bd=2,
    command=salir_ventana,
)
boton_salir.place(x=340, y=25)

frame_resultados = tk.Frame(ventana_principal)
frame_resultados.config(background="#64b446", width=480, height=110)
frame_resultados.place(x=10, y=290)

texto_resultados = tk.Text(frame_resultados)
texto_resultados.config(width=45, height=4, state="disabled", font=("Consolas", 14))
texto_resultados.place(x=11, y=14)

ventana_principal.mainloop()
