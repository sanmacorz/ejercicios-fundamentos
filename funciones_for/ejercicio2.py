# Construir una función que reciba una cadena digitada por el usuario y que lo muestre n veces en la pantalla.

def MostrarNombre(nombre, veces):
    for i in range(0, veces):
        print(nombre)
    return nombre

nombre = input("Ingrese su nombre: ")
n_veces = int(input("Ingrese la cantidad de veces: "))
print(MostrarNombre(nombre, n_veces))