#!/usr/bin/env python3
# Realizar diferentes operaciones a las siguientes tres listas utilizando los varios métodos existentes

a = ["Pedro", 555, "Python", "Intel", "HP"]
b = [45, -67.8, 999.99, -2702.0, 1858]
c = ["mouse", "teclado"]

print(len(a))  # Calcula la cantidad de elementos dentro de una lista
print(max(b))  # Calcula el número entero de mayor valor dentro de una lista
print(min(b))  # Calcula el número entero de menor valor dentro de una lista
a.extend(c)  # Agrega todos los elementos de una lista a otra
a.append(-2015)  # Agrega un elemento con valor -2015 a la última posición de una lista
b.insert(2, 47)  # Agrega un elemento con valor 47 a la tercera posición de una lista
b.pop()  # Elimina el último elemento de una lista
b.pop(3)  # Elimina el elemento con índice 3 de una lista
b.remove(45)  # Elimina el elemento con valor 45 de una lista
a.sort()  # Organiza todos los elementos de una lista ascendentemente
a.reverse()  # Organiza todos los elementos de una lista al réves
