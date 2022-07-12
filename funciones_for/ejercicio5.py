#!/usr/bin/env python3
# Construir una función que reciba como parametro una lista de datos númericos y retorne el promedio de datos pares.


def sumatoria_lista(lista):
    lista_pares = []
    sumatoria = 0
    for numeros in lista:
        if (numeros % 2) == 0:
            lista_pares.append(numeros)
    for elemento in lista_pares:
        sumatoria += elemento
    resultado = int(sumatoria / len(lista_pares))
    return resultado


print(
    "El promedio de los números pares entre 1 y 10 es de "
    + str(sumatoria_lista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
)
