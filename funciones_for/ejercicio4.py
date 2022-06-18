# Construir una función que reciba como parametro una lista de datos númericos y retorne el promedio de dichos datos.

def SumatoriaLista(lista):
    k = len(lista)
    for i in lista:
        i += i
    return(int(i / k))

print(SumatoriaLista([1, 2, 3]))