#!/usr/bin/env python3
# Genere mil números aleatorios, y averigüe cuántos son pares y cuántos son impares.

import random

n = int(input("Ingrese un número: "))
contador_par = 0
contador_impar = 0
resultado = []

for i in range(n):
    numero = random.randint(0, 100)
    resultado.append(str(numero))
    if (numero % 2) == 0:
        contador_par += 1
    else:
        contador_impar += 1
        
# Imprimir una lista
print(', '.join(resultado))
print("Hay " + str(contador_par) + " números pares y " + str(contador_impar) + " números impares!")