#!/usr/bin/env python3
# Hacer el diagrama de flujo y el programa en Python, que lea un capital "c", y que averigue e imprima, en cuántos meses se duplica, si lo colocamos a un interes compuesto del 5% mensual.

capital = int(input("Ingrese el capital inicial que desee invertir: "))
doble = capital * 2
meses = 0

while capital <= doble:
    capital = capital + (capital * 0.05)
    meses += 1

print("La cantidad de meses necesarios para duplicar el capital inicial es de " + str(meses) + " meses.")