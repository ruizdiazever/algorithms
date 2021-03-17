# EXERCISE 2.7

def domino():
    """ Este algoritmo imprime las fichas del domino, es una negrada, soy conciente de ello. """

    aux = 6
    lista = []
    
    for i in range(1, 29):
        if (i >= 1  and i <= 7):
            print(f"Ficha ({i:02d}) ->     {0} | {i - 1}")
            lista.append({0} | {i - 1})
        elif (i >= 7  and i <= 13):
            print(f"Ficha ({i:02d}) ->     {1} | {(i - 1) - aux}")
            lista.append({1} | {(i - 1) - aux})
        elif (i >= 13  and i <= 18):
            print(f"Ficha ({i:02d}) ->     {2} | {(i) - (aux*2)}")
        elif (i >= 18  and i <= 22):
            print(f"Ficha ({i:02d}) ->     {3} | {(i + 2) - (aux*3)}")
        elif (i >= 22  and i <= 25):
            print(f"Ficha ({i:02d}) ->     {4} | {(i + 5) - (aux*4)}")
        elif (i >= 25  and i <= 27):
            print(f"Ficha ({i:02d}) ->     {5} | {(i + 9) - (aux*5)}")
        elif (i >= 27  and i <= 28):
            print(f"Ficha ({i:02d}) ->     {6} | {(i + 14) - (aux*6)}")

# Second version of this exercise
def dominoSuper():
    for i in range(7):
        for x in range(i, 7):
            print(f"{i}:{x}")

test = dominoSuper()