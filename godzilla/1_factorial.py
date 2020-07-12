# Ejercicio 1.3
def iterador():
    # Multiplicacion de iterador por iterador
    for i in range(5): 
        print(i * i)

def raiz():
    # Raiz cuadrada segun iterador
    for i in range(2, 6): 
        print(i, 2 **i)

def factorial(num):
    if num > 0:
        num = num * factorial(num - 1)
    else:
        num = 1
    return num
