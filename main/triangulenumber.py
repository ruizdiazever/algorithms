# EXERCISE 2.5

from time import time
def count_elapsed_time(f):
    """
    Decorator.
    Execute the function and calculate the elapsed time.
    Print the result to the standard output.
    """
    def wrapper():
        # Start counting.
        start_time = time()
        # Take the original function's return value.
        ret = f()
        # Calculate the elapsed time.
        elapsed_time = time() - start_time
        print("Elapsed time: %0.10f seconds." % elapsed_time)
        return ret
    
    return wrapper

# This algorithm is mineeeee
@count_elapsed_time
def triangule_numbers():
    """
    Induccion matematica, suma de los números naturales desde 1 hasta num
    Algoritmo original propio.
    """
    num = int(input("Please input one integer number: "))
    lista = []

    for i in range(1, num + 1, 1):
        lista.append(i)
        print(f"{i} - {sum(lista)}")

# Internet algorithm based on the equation
@count_elapsed_time
def triangule_numbers_2():
    """
    Induccion matematica, suma de los números naturales desde 1 hasta num
    Algoritmo basado en ecuacion.
    """
    num = int(input("Please input one integer number: "))

    for i in range(1, num + 1, 1):
        print(f"{i} - {int(i * (i + 1) / 2)}")