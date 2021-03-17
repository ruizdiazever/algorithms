# EXERCISE 2.8
def programGame():
    num = int(input("Input the limit number of game: "))

    for i in range(num + 1):
        for x in range(i, num + 1):
            print(f"{i}:{x}")

test = programGame()