# Ecuación de segundo grado usando funciones

import math

def hallar_discriminante(a, b1, c):
    d = math.sqrt(b1*b1 - 4*a*c)
    return d

a = float(input("Ingrese el coeficiente de x²: "))
b = float(input("Ingrese el coeficiente de x: "))
c = float(input("Ingrese el termino independiente: "))

d1 = hallar_discriminante(a, b, c)

x1 = (-b + d1) / 2 * a
x2 = (-b - d1) / 2 * a

print("La primera raíz es: " + str(x1) + " y la segunda es " + str(x2))