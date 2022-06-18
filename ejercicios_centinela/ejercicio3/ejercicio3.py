#!/usr/bin/env python3
# Calcular el número de billetes necesarios para cada cheque, e imprimir cuántos billetes quedan al final del día

total_billetes_1 = 0
total_billetes_2 = 0
total_billetes_3 = 0
valor_cheque = int(input("Ingrese el valor total del cheque: "))

while valor_cheque != 0:
    billetes_1 = valor_cheque // 10000
    reserva = valor_cheque - (billetes_1 * 10000)
    billetes_2 = reserva // 2000
    reserva = reserva - (billetes_2 * 2000)
    billetes_3 = reserva // 100
    total_billetes_1 = total_billetes_1 + billetes_1
    total_billetes_2 = total_billetes_2 + billetes_2
    total_billetes_3 = total_billetes_3 + billetes_3
    print("El valor del cheque es de " + str(valor_cheque))
    print("Necesita " + str(billetes_1) + " billetes de $10.000")
    print("Necesita " + str(billetes_2) + " billetes de $2.000")
    print("Necesita " + str(billetes_3) + " monedas de $100")
    valor_cheque = int(input("Ingrese el valor total del cheque: "))
else:
    print("Fin de los datos de entrada!")
    print("Se gastaron " + str(total_billetes_1) + " billetes de $10.000, " + str(total_billetes_2) + " billetes de $2.000 y " + str(total_billetes_3) + " monedas de $100 en total al final del día.")