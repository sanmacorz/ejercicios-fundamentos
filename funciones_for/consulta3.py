#!/usr/bin/env python3
# Funciones lambda

# Definiendo dos listas con diferentes tipos de elementos

numeros = [1, 2, 3, 4, 5]
strings = ['apple', 'and', 'a', 'donut']

# Una expresión lambda de una sola línea que duplica todos los elementos de una lista

doble = list(map(lambda n: n * 2, numeros))

for numero in doble:
    print(numero)

# Una expresión lambda completa (definida dentro de una función) que duplica todos los elementos de una lista

def double(n):
    return n * 2

doble = list(map(double, numeros))

for numero in doble:
    print(numero)
    
# Una expresión lambda de una sola línea que imprime solo los elementos de una lista los cuáles tengan una longitud mayor de 3

palabras = list(filter(lambda s: len(s) > 3, strings))

for palabra in palabras:
    print(palabra)