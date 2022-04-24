#!/usr/bin/env python3
# Ejercicio 2. Crear un programa para obtener la división normal, el módulo, y la división entera de un número

x = int(input("Introduzca el dividendo: "))
y = int(input("Introduzca el divisor: "))
z1 = (x / y)
z2 = (x % y)
z3 = (x // y)
print("La división es: " + str(z1) + "\n El módulo es: " + str(z2) + "\n La división como entero es: " + str(z3))