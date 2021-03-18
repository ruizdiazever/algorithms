# EXERCISE 2.6, factorial of a list of numbers.

def multi_list(lista):
    multi= 1

    for i in range(0, len(lista)):
        multi = multi * lista[i]
    return multi

def factorial():
    """ Cantidad pedido al usuario, imprime el factorial de cada numero hasta el ingresado. """
    num = int(input("Please input one integer number: "))
    lista = []

    for i in range(1, num + 1, 1):
        lista.append(i)
        
    multi = multi_list(lista)
    print(f"{i} ---> {multi}")