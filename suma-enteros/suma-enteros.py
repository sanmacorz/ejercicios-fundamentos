#!/usr/bin/env python3
# Ejercicio 1. Crear un programa para sumar dos números enteros.

# Define la variable "numero1" como un entero (int) y crea una input para preguntar por el valor deseado de este número. (INPUT-STORAGE)
x = int(input("Ingrese el primer numero: "))
# Define la variable "numero2" como un entero (int) y crea una input para preguntar por el valor deseado de este número. (INPUT-STORAGE)
y = int(input("Ingrese el segundo numero: "))
# Define la variable "resultado" y asigna el valor de la operación de las dos variables anteriores. (PROCESSING)
z = (x + y)
# Lee el valor de la variable "resultado" y lo imprime en pantalla. (OUTPUT)
print("La suma de "+ str(x) + " y " + str(y) + " es: " + str(z))