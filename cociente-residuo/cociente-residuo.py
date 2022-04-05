#!/usr/bin/env python3
# Ejercicio 2. Crear un programa para obtener la división normal, el módulo, y la división entera de un número.

# Define la variable "x" como un entero (int) y crea una input para preguntar por el valor deseado de este número. (INPUT-STORAGE)
x = int(input("Introduzca el dividendo: "))
# Define la variable "y" como un entero (int) y crea una input para preguntar por el valor deseado de este número. (INPUT-STORAGE)
y = int(input("Introduzca el divisor: "))
# Define la variable "z1" y le asigna el valor de la operación entre los dos números. (PROCESSING-STORAGE)
z1 = (x / y)
# Define la variable "z2" y le asigna el valor de la operación entre los dos números. (PROCESSING-STORAGE)
z2 = (x % y)
# Define la variable "z3" y le asigna el valor de la operación entre los dos números. (PROCESSING-STORAGE)
z3 = (x // y)
# Lee el valor de la variable "z1", "z2", y "z3" y lo imprime en pantalla. (OUTPUT)
print("La división es: " + str(z1) + "\n El módulo es: " + str(z2) + "\n La división como entero es: " + str(z3))