# EXERCISE 2.4

def pairs():
    """ Imprime todos los numeros pares entre 2 numeros introducidos. """
    num_1 = int(input("Please input one number: "))
    num_2 = int(input("Please input other number: "))

    if num_1 < num_2:
        for i in range(num_1, num_2 + 1, 2):
            if i % 2 == 0:
                print(i)
            else:
                print(i+1)
    else:
        for i in range(num_1, num_2 - 2, -2):
            if i % 2 == 0:
                print(i)
            else:
                print(i+1)