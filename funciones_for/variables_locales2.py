def f(x):
    x += 1
    print("Valor de x dentro de f(x) = ", x)
    return(x)

x = 3
print("Valor inicial de x = ", x)
z = f(x)
print("Valor de x despues de llamar a f(x) = ", x)