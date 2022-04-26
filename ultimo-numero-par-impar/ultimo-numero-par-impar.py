#!/usr/bin/env python3
# Ejercicio 6. Crear un programa para determinar si un número es par o impar

n = int(input("Ingrese un número: "))
u = (n % 10)

if (u % 2) == 0:
    z = "El número es par"
    print(z)
else:
    z = "El número es impar"
    print(z)