# EXERCISE 2.8, dominoes extend.

def dominoPlus():
    """ This algorithm print the dominoes. """

    num = int(input("Input the limit number of game: "))

    for i in range(num + 1):
        for x in range(i, num + 1):
            print(f"{i}:{x}")

test = dominoPlus()