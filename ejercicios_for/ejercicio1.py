#!/usr/bin/env python3

# Utilizando la forma habitual de iterar con un ciclo while
suma = 0
contador = 1

while contador <= 10:
    suma += contador
    contador += 1
print(suma)

# Utilizando un ciclo for a manera de contador
suma = 0

for i in range(0, 11):
    suma += i
print(suma)