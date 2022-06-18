#!/usr/bin/env python3
# Calcular e imprimir la serie de Fibonacci a partir de enésimos términos dados


def serie_fibonacci(terminos):
    resultado = []
    primer_termino = 1
    resultado.append(str(primer_termino))
    segundo_termino = 1
    resultado.append(str(segundo_termino))

    # Se descartan los dos términos que ya se agregaron
    for numero in range(terminos - 2):
        total = primer_termino + segundo_termino
        segundo_termino = primer_termino
        primer_termino = total
        resultado.append(str(total))
    return resultado


numero_terminos = int(input("Ingrese el número de términos que desee: "))
print(", ".join(serie_fibonacci(numero_terminos)))
