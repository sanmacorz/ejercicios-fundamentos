#!/usr/bin/env python3
# Convertir distintas monedas a dólares usando funciones

def convertir_moneda(tipo_pesos, valor_dolar):
    pesos = float(input("Cuántos pesos " + str(tipo_pesos) + " tienes?"))
    dolares = str(round(pesos / valor_dolar, 2))
    return dolares

def funcion_principal():
    opcion = input("""---CONVERSOR DE MONEDAS---
1. Pesos Colombianos
2. Pesos Argentinos
3. Pesos Mexicanos
Elige una opción: """)
    if opcion == "1":
        print(convertir_moneda("COP", 3966.60))
    elif opcion == "2":
        print(convertir_moneda("ARS", 122.52))
    elif opcion == "3":
        print(convertir_moneda("CLP", 869.25))
    else:
        print("Ingrese una opción válida!")

if __name__ == "__main__":
    funcion_principal()