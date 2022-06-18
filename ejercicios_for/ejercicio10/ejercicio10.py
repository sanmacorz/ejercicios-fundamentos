#!/usr/bin/env python3
# Generar la siguiente serie: [3, 8, 13, 18, 23, 28, ... n]

n = int(input("Ingrese un número n de veces: "))

resultado = []

for i in range(1, (n + 1)):
    resultado.append(str(5 * i - 2))
print(', '.join(resultado))