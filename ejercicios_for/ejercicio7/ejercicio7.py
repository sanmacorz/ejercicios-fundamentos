#!/usr/bin/env python3
# Diagrama de flujo y programa en Python que averigue e imprima cuántos multiplos de 7 y cuántos multiplos de 9, hay en los números compredidos entre el 1000 y el 5000.

inicio_rango = int(input("Ingrese un número para el inicio del rango: "))
final_rango = int(input("Ingrese un número para el final del rango: "))

multiplos_siete = 0
multiplos_nueve = 0

for numero in range(inicio_rango, (final_rango + 1)):
    if (numero % 7) == 0:
        multiplos_siete += 1
    elif (numero % 9) == 0:
        multiplos_nueve += 1

print("Hay " + str(multiplos_siete) + " múltiplos de siete y " + str(multiplos_nueve) + " múltiplos de nueve!")