#!/usr/bin/env python3
# Programa que permite simular el lanzamiento de n dados, y que muestre en forma de histograma la frecuencia con la que salió cada una de los 6 números. (con el #)

import random

contador_1 = ""
contador_2 = ""
contador_3 = ""
contador_4 = ""
contador_5 = ""
contador_6 = ""

n_dados = int(input("Ingrese la cantidad de dados que quiere lanzar: "))

for dados in range(n_dados):
    resultado_dado = random.randint(1, 6)
    if resultado_dado == 1:
        contador_1 += "#"
    elif resultado_dado == 2:
        contador_2 += "#"
    elif resultado_dado == 3:
        contador_3 += "#"
    elif resultado_dado == 4:
        contador_4 += "#"
    elif resultado_dado == 5:
        contador_5 += "#"
    elif resultado_dado == 6:
        contador_6 += "#"
        
print("1: " + contador_1 + "\n" + "2: " + contador_2 + "\n" + "3: " + contador_3 + "\n" + "4: " + contador_4 + "\n" + "5: " + contador_5 + "\n" +"6: " + contador_6)