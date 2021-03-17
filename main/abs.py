# EXERCISE 4.2

def abspersonal():
    num = int(input('Please, input a integer number: '))
    aux = 0

    if num > 0:
        aux = num
    elif num < 0:
        aux = -(num)

    print(aux)

abspersonal()