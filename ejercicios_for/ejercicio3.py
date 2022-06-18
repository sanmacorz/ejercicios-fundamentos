#!/usr/bin/env python3

# Itera por una string 
nombre = input("Ingrese su nombre: ")
for letra in nombre:
    print(letra)
    
# Itera por una string y aplica un condicional
nombre = input("Ingrese su nombre: ")
for letra in nombre:
    if letra == "o":
        print("#")
    else:
        print(letra)
        
# Itera por una string y aplica un método
nombre = input("Ingrese su nombre: ")
for letra in nombre:
    print(letra.upper())