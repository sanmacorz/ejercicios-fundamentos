#!/usr/bin/env python3
# Calcular el número de billetes necesarios para cada cheque, e imprimir cuántos billetes quedan al final del día

tb1 = 0
tb2 = 0
tb3 = 0
ch = int(input("Ingrese el valor total del cheque: "))

while ch != 0:
    b1 = ch // 10000
    r = ch - (b1 * 10000)
    b2 = r // 2000
    r = r - (b2 * 2000)
    b3 = r // 100
    tb1 = tb1 + b1
    tb2 = tb2 + b2
    tb3 = tb3 + b3
    print("El valor del cheque es de " + str(ch))
    print("Necesita " + str(b1) + " billetes de $10.000")
    print("Necesita " + str(b2) + " billetes de $2.000")
    print("Necesita " + str(b3) + " monedas de $100")
    ch = int(input("Ingrese el valor total del cheque: "))
else:
    print("Fin de los datos de entrada!")
    print("Se gastaron " + str(tb1) + " billetes de $10.000, " + str(tb2) + " billetes de $2.000 y " + str(tb3) + " monedas de $100 en total al final del día.")