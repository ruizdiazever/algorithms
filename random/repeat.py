import random

def test(num):
    lista = []

    for i in range(num):
        lista.append(random.randrange(10))
    
    for i in lista:
        if i == i:
            repetido = i
        popular = lista.count(i)

    print("LISTA: ", lista)
    print("MAS POPULAR: ", repetido,"tiene", popular, "repeticiones.")