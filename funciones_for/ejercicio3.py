# Construir una función que reciba como parametro una lista de datos numéricos y retorne la suma de dichos datos.

def SumatoriaLista(lista):
    for i in lista:
        i += i
    return(i)

print(SumatoriaLista([1, 2, 3]))