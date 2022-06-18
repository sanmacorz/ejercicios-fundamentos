#!/usr/bin/env python3

# Itera por los 10 primeros enteros, empezando desde el cero.
for i in range(10):
    print(i)

# Itera por los 10 primeros enteros, empezando desde el uno.
for i in range(1, 11):
    print(i)

# Itera por los 10 primeros enteros, empezando desde el uno, e imprime una string.
for i in range(1, 11):
    print("Hola!")

# Itera por los 10 primeros enteros, e imprime dos strings concatenadas.
for i in range(10):
    print("i = " + str(i))

# Itera por los 10 primeros enteros, e imprime dos strings formateadas.
for i in range(10):
    print(f"i = {i}")

# Itera por los 5 primeros enteros, empezando desde el menos ocho hasta el menos trece, disminuyendo uno.
for i in range(-8, -13, -1):
    print(f"i = {i}")