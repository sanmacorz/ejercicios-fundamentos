#!/usr/bin/env python3
# Un acrónimo es una palabra formada con las iniciales de una frase. Por ejemplo, ROM es el acrónimo de Read Only Memory. Diseñe un programa que lea una frase y despliegue el acrónimo. Las letras del acrónimo deben ser mayúsculas.

frase = input("Ingrese la frase: ")

for letra in frase.split():
    print(letra[0].upper())
