#!/usr/bin/env python3
# Calcule e imprima en qué año la población de la ciudad A es mayor que la de la ciudad B

año = 1980
poblacion_a = 3.5
tasa_a = 0.07
poblacion_b = 5
tasa_b = 0.05

while poblacion_a < poblacion_b:
    poblacion_a += (poblacion_a * tasa_a)
    poblacion_b += (poblacion_b * tasa_b)
    año += 1
    
print("En el año " + str(año) + " la población de la ciudad A de " + str(round(poblacion_a, 1)) + " millones de habitantes superó a la población de la ciudad B de " + str(round(poblacion_b, 1)) + " millones de habitantes.")