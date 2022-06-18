# Construir una función que reciba como parametro una lista de datos númericos y retorne el promedio de datos pares.

def SumatoriaLista(lista):
    lista_pares = []
    for numeros in lista:
        if (numeros % 2) == 0:
            lista_pares.append(numeros)
    print(lista_pares)
    k = len(lista_pares)
    wat = 0
    for wat in lista_pares:
        print(wat)
        resultado = wat + wat
    #resultado = pares + pares
    print(resultado)
    # return(pares / k)

print(SumatoriaLista([5, 6, 7, 8]))