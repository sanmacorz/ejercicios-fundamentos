#!/usr/bin/env python3
# Llamados por valor y por referencia

# Llamado por valor
def doblar_valor(numero):
    numero *= 2
n = 10
doblar_valor(n)
print(n)


# Llamado por referencia
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [10,50,100]
doblar_valores(ns)
print(ns)
