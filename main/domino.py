# EXERCISE 2.7, dominoes

def domino():
    """ This algorithm print the dominoes. """
    for i in range(7):
        for x in range(i, 7):
            print(f"{i}:{x}")

test = domino()