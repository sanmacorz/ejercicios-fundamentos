#!/usr/bin/env python3
# Realice un programa que implemente el juego de los números donde el usuario va a escoger un número entero generado de manera aleatoria.

import random

exito = False
intentos = 0
nombre = input("Hola, ¿cómo te llamas? ")
numero = random.randint(1, 20)

while exito == False:
    intentos += 1
    intento = int(input("Muy bien " + nombre + ", adivina el número entre 1 y 20: "))
    if intento == numero:
        print(
            "Buen trabajo " + nombre + ", acertaste en " + str(intentos) + " intentos."
        )
        exito = True
    if intento > numero:
        print("Tú número es muy alto. Dame otro número")
    elif intento < numero:
        print("Tú número es muy bajo. Dame otro número")
