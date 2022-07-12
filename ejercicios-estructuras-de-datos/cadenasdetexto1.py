#!/usr/bin/env python3
# Se desea saber cuantas veces en la palabra colombiano se encuentra el caracter o. Además, deseamos que se despliegue el mensaje sudamericano en cada ocasión que se encuentre el caracter deseado.

palabra = "Colombiano".lower()
total_veces = 0

for letra in palabra:
    if letra == "o":
        print("Sudamericano")
        total_veces += 1
print("Se encontró un total de " + str(total_veces) + " veces el caracter deseado.")
