#!/usr/bin/env python3
import tkinter as tk
import random


def calcular_ganador_piedra():
    eleccion_jugador = "Piedra"
    eleccion_cpu = random.randint(0, 2)

    if eleccion_jugador == "Piedra" and eleccion_cpu == 0:
        imagen_respuesta.configure(image=imagen_piedra)
        resultado = "Empate"

    elif eleccion_jugador == "Piedra" and eleccion_cpu == 1:
        imagen_respuesta.configure(image=imagen_papel)
        resultado = "Derrota"
        label_puntaje_cpu.configure(text=int(label_puntaje_cpu.cget("text")) + 1)

    elif eleccion_jugador == "Piedra" and eleccion_cpu == 2:
        imagen_respuesta.configure(image=imagen_tijera)
        resultado = "Victoria"
        label_puntaje_jugador.configure(
            text=int(label_puntaje_jugador.cget("text")) + 1
        )

    label_resultado.configure(text=resultado)


def calcular_ganador_papel():
    eleccion_jugador = "Papel"
    eleccion_cpu = random.randint(0, 2)

    if eleccion_jugador == "Papel" and eleccion_cpu == 0:
        imagen_respuesta.configure(image=imagen_piedra)
        resultado = "Victoria"
        label_puntaje_jugador.configure(
            text=int(label_puntaje_jugador.cget("text")) + 1
        )

    elif eleccion_jugador == "Papel" and eleccion_cpu == 1:
        imagen_respuesta.configure(image=imagen_papel)
        resultado = "Empate"

    elif eleccion_jugador == "Papel" and eleccion_cpu == 2:
        imagen_respuesta.configure(image=imagen_tijera)
        resultado = "Derrota"
        label_puntaje_cpu.configure(text=int(label_puntaje_cpu.cget("text")) + 1)
    label_resultado.configure(text=resultado)


def calcular_ganador_tijera():
    eleccion_jugador = "Tijera"
    eleccion_cpu = random.randint(0, 2)

    if eleccion_jugador == "Tijera" and eleccion_cpu == 0:
        imagen_respuesta.configure(image=imagen_piedra)
        resultado = "Derrota"
        label_puntaje_cpu.configure(text=int(label_puntaje_cpu.cget("text")) + 1)

    elif eleccion_jugador == "Tijera" and eleccion_cpu == 1:
        imagen_respuesta.configure(image=imagen_papel)
        resultado = "Victoria"
        label_puntaje_jugador.configure(
            text=int(label_puntaje_jugador.cget("text")) + 1
        )

    elif eleccion_jugador == "Tijera" and eleccion_cpu == 2:
        imagen_respuesta.configure(image=imagen_tijera)
        resultado = "Empate"

    label_resultado.configure(text=resultado)


ventana_principal = tk.Tk()
ventana_principal.geometry("500x800")
ventana_principal.resizable(False, False)
ventana_principal.configure(
    background="#9BC4BC", highlightbackground="black", highlightthickness=8
)

label_titulo = tk.Label(
    text="Piedra, papel o tijera!",
    background="#9BC4BC",
    foreground="#090909",
    font=("Verdana", 20, "bold"),
)
label_titulo.place(x=90, y=20)

label_puntaje_cpu = tk.Label(
    text=0, background="#9BC4BC", foreground="#4B5043", font=("Consolas", 30, "bold")
)
label_puntaje_cpu.place(x=380, y=70)

label_puntaje_jugador = tk.Label(
    text=0, background="#9BC4BC", foreground="#4B5043", font=("Consolas", 30, "bold")
)
label_puntaje_jugador.place(x=120, y=70)

imagen_piedra = tk.PhotoImage(file="piedra.png")
boton_piedra = tk.Button(
    ventana_principal,
    background="white",
    image=imagen_piedra,
    borderwidth=5,
    relief="raised",
    command=calcular_ganador_piedra,
)
boton_piedra.place(x=55, y=125)

imagen_papel = tk.PhotoImage(file="papel.png")
boton_papel = tk.Button(
    ventana_principal,
    background="white",
    image=imagen_papel,
    borderwidth=5,
    relief="raised",
    command=calcular_ganador_papel,
)
boton_papel.place(x=55, y=310)

imagen_tijera = tk.PhotoImage(file="tijera.png")
boton_tijera = tk.Button(
    ventana_principal,
    background="white",
    image=imagen_tijera,
    borderwidth=5,
    relief="raised",
    command=calcular_ganador_tijera,
)
boton_tijera.place(x=55, y=550)

label_resultado = tk.Label(
    text="", background="#9BC4BC", foreground="#4B5043", font=("Verdana", 15, "bold")
)
label_resultado.place(x=220, y=75)

imagen_respuesta = tk.Label(image="", background="#9BC4BC")
imagen_respuesta.place(x=320, y=310)

label_firma = tk.Label(
    text="[smc]", background="#9BC4BC", font=("monospace", 20, "bold")
)
label_firma.place(x=400, y=740)

ventana_principal.mainloop()
