#!/usr/bin/env python3
# Ejercicio 8. Programa para determinar si dados tres números enteros, la suma de los dos primeros es igual al tercero.

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

if (numero1 + numero2) == numero3:
    iguales = "La suma de los números " + str(numero1) + " y " + str(numero2) + " es igual a " + str(numero3)
else:
    iguales = "La suma de los números " + str(numero1) + " y " + str(numero2) + " es diferente a " + str(numero3)
    
print(iguales)