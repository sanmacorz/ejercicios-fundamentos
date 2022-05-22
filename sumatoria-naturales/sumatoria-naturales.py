#!/usr/bin/env python3
# Calcular la sumatoria de una cierta cantidad de números naturales

n = int(input("Ingrese los enésimos números: "))
k = 1
suma = 0

while k <= n:
    suma += k
    k += 1

print("La suma de los " + str(n) + " primeros valores naturales es de " + str(suma))