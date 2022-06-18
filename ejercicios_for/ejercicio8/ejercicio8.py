#!/usr/bin/env python3
# Diagrama de flujo y programa en Python que lea un número entero positivo, que calcule su factorial, y que lo imprima junto a su número leído. (con for loop)

numero = int(input("Ingrese un número: "))
resultado = 1

for i in range(1, numero + 1):
    resultado *= i
    
print("El factorial de " + str(numero) + " es " + str(resultado))
