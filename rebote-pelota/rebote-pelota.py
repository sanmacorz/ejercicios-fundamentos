#!/usr/bin/env python3
# Una pelota se deja caer desde una altura h, y en cada rebote sube el 10% menos que el anterior. Calcule e imprima en cuál rebote la pelota no alcanza a subir la quinta parte de la altura inicial.

h = int(input("Ingrese la altura de la pelota: "))

rebotes = 0
quinta = (h / 5)

while h >= quinta:
    h = h - (h * 0.10)
    rebotes += 1
    print("La altura " + str(round(h, 1)) + " se alcanza en el rebote " + str(rebotes))
  
print("El número de rebotes necesarios para que la altura sea menor que la quinta parte de la altura inicial es de " + str(rebotes) + " rebotes.")