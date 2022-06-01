#!/usr/bin/env python3
# Calcule e imprima cuándo unos números son pares y cuando son impares. Para terminar, utilizaremos el registro centinela, cuando el valor del número leído sea cero.

n = int(input("Ingrese un número: "))
par = 0
impar = 0

while n != 0:
    d = n % 2
    
    if d == 0:
        impar += 1
    else:
        par += 1
        
    n = int(input("Ingrese un número: "))
else:
    print("Fin de los datos de entrada!")
    print("Los números impares son: " + str(impar) + " y los números pares son: " + str(par))