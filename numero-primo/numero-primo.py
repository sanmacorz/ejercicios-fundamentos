#!/usr/bin/env python3
# Cree un programa que lea un número y determine a través de un ciclo while si este es un número primo o no.

numero = int(input("Ingrese un número: "))
i = 2
bandera = False

if numero > 1:
    while i < numero:
        if (numero % i) == 0:
            bandera = True
        i += 1
else:
    print("El número " + str(numero) + " es compuesto!")
    
if bandera == True:
    print("El número " + str(numero) + " es compuesto!")
else:
    print("El número " + str(numero) + " es primo!")