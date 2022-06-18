#!/usr/bin/env python3
# Digite su nombre y cuente cuántas vocales hay en él

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

nombre = input("Ingrese su nombre: ")

for letra in nombre:
    if letra == "a":
        contador_a += 1
    elif letra == "e":
        contador_e += 1
    elif letra == "i":
        contador_i += 1
    elif letra == "o":
        contador_o += 1
    elif letra == "u":
        contador_u += 1

print("Su nombre tiene " + str(contador_a) + " veces la vocal a, "  + str(contador_e) + " veces la vocal e, " + str(contador_i) + " veces la vocal i, " +  str(contador_o) + " veces la vocal o," + " y " + str(contador_u) + " veces la vocal u!")