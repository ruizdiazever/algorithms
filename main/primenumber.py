# EXERCISE 4.1

def oddOrEvenNumber():
    num = int(input("Please, input a integer number: "))

    if (num % 2 == 0):
        print(f"The number {num} is  a EVEN number.")
    else:
        print(f"The number {num} in a ODD number.")


def primeNumber():
    """Los números primos son aquellos que solo son divisibles entre ellos mismos y el 1 dando 0 de residuo"""
    num = int(input("Please, input a integer number: "))
    aux = 0

    for i in range(1, num+1):
        if (num % i == 0):
            aux += 1
        else:
            pass

    if aux > 2:
        print('NUMERO COMPUESTO')
    else:
        print('NUMERO PRIMO')