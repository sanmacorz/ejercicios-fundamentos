#!/usr/bin/env python3
# Variables locales y globales

# Variable local
def sumar(sumando1, sumando2):
	suma = sumando1 + sumando2
	return suma
print(sumar(4, 5))
# print(suma)

# Variable global
def saludar():
	print(saludo)
saludo = "Hola Mundo!"
print(saludar())
# print(saludo)