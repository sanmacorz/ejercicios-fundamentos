#!/usr/bin/env python3
# Lea el código, y el nombre, y las notas de los tres parciales de una materia, y que calcule e imprima el código, el nombre, y la nota final de cada estudiante.

con = 0
cod = int(input("Ingrese el código del estudiante: "))

if cod != 0:
    nombre = str(input("Ingrese el nombre del estudiante: "))
    nota1 = float(input("Ingrese la primera nota del estudiante: "))
    nota2 = float(input("Ingrese la segunda nota del estudiante: "))
    nota3 = float(input("Ingrese la tercera nota del estudiante: "))
else:
    print("Fin de los datos de entrada!")
    
while cod != 0:
    notafin = (nota1 + nota2 + nota3) / 3
    print("El estudiante " + str(nombre) + " con código " + str(cod) + " tuvo una nota defintiva de " + str(round(notafin, 1)))
    
    if notafin < 3.0:
        con += 1
        print("La cantidad de estudiantes que reprobaron la materia fue de: " + str(con))
        
    cod = int(input("Ingrese el código del estudiante: "))

    if cod != 0:
        nombre = str(input("Ingrese el nombre del estudiante: "))
        nota1 = float(input("Ingrese la primera nota del estudiante: "))
        nota2 = float(input("Ingrese la segunda nota del estudiante: "))
        nota3 = float(input("Ingrese la tercera nota del estudiante: "))
else:
    print("Fin de los datos de entrada!")