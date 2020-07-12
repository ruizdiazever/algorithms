# Ejercicio 1.3
def iterador():
    for i in range(5): # Multiplicacion de iterador por iterador
        print(i * i)

def raiz():
    for i in range(2, 6): # Raiz cuadrada segun iterador
        print(i, 2 **i)

def factorial(num):
    if num > 0:
        num = num * factorial(num - 1)
    else:
        num = 1
    return num
