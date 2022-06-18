# Construir una función que reciba su nombre como parametro y que lo muestre 5 veces en la pantalla.

def MostrarNombre(nombre):
    for i in range(0, 5):
        print(nombre)
    return nombre

nombre = input("Ingrese su nombre: ")
print(MostrarNombre(nombre))