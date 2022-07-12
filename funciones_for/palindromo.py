#!/usr/bin/env python3
# Determinar e imprimir si una palabra dada es palíndromo o no


def es_palindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False


# Otra forma de hacerlo, revirtiendo la lista y comparando la lista revertida con la normal
# for i in reversed(palabra):
#    print(i)

palabra = str(input("Ingrese una palabra que desee: "))

if es_palindromo(palabra) == True:
    print("SÍ es un palíndromo")
else:
    print("NO es un palíndromo")
