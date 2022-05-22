#!/usr/bin/env python3
# Cree un programa que lea dos números enteros y averigue si uno es múltiplo del otro.

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1 > numero2:
    if (numero1 % numero2) == 0:
        print("El número " + str(numero1) + " SÍ es múltiplo de " + str(numero2))
    else:
        print("El número " + str(numero1) + " NO es múltiplo de " + str(numero2))
else:
    if (numero2 % numero1) == 0:
        print("El número " + str(numero2) + " SÍ es múltiplo de " + str(numero1))
    else:
        print("El número " + str(numero2) + " NO es múltiplo de " + str(numero1))