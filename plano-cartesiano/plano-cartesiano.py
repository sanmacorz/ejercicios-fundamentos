#!/usr/bin/env python3
# Ejercicio 5. Crear un programa para calcular el cuadrante de un punto en un plano cartesiano

x = int(input("Ingrese la coordenada x: "))
y = int(input("Ingrese la coordenada y: "))

if x > 0 and y > 0:
    z = "El cuadrante del punto es el I."
    print(z)
elif x < 0 and y > 0:
    z = "El cuadrante del punto es el II."
    print(z)
elif x < 0 and y < 0:
    z = "El cuadrante del punto es el III."
    print(z)
elif x > 0 and y < 0:
    z = "El cuadrante del punto es el IV."
    print(z)
elif x > 0 or x < 0 and y == 0:
    z = "El punto se encuentra en el eje x"
    print(z)
elif x == 0 and y > 0 or y < 0:
    z = "El punto se encuentra en el eje y."
    print(z)
elif x == 0 and y == 0:
    z = "El punto se encuentra en el origen del plano."
    print(z)
else:
    z = "Por favor digite unas coordenadas válidas."
    print(z)