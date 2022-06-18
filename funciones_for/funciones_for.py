a = int(input("Ingrese el número a buscar: "))
b = [1, 2, 3, 4, 5]
    
def BuscarDato(dato, lista):
    if dato in lista:
        return("Lo encontré!")
    else:
        return("No lo encontré!")
        
print(BuscarDato(a, b))