# EXERCISE 2.1

def credit():
    coin = float(input("Ingrese la cantidad del prestamo en euros: "))
    interest = float(input("Introduzca la tasa de interes: "))
    years = int(input("Ingrese la cantidad de años: "))

    final_coin = coin * (1 + ((interest / 100) ** years))

    print(f"El monton final a pagar es: {final_coin}")




# EXERCISE 2.2

class Temperature:
    """ Toma una temperatura en Fahrenheit y retorna en Celsius y viceversa. """

    def __init__(self):
        print("Welcome to the converter of temperature.")

    # Fahrenheit to Celsius
    def fahrenheit_to_celsius(self, num):
        self.num = num

        celsius = (num - 32) * 5/9
        return celsius
    
    # Celsius to Fahrenheit
    def celsius_to_fahrenheit(self, num):
        self. num = num

        fahrenheit = (num * 1.8) + 32
        return fahrenheit




# EXERCISE 2.3

def temperature_table_10():
    """ Devuelve valores en Celsius de 0 a 120 Fahrenheit con una franja de 10 grados F°. """
    for i in range (0, 120, 10):
        print(f"{i} Fahrenheit = {test.fahrenheit_to_celsius(i)} Celsius.")





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






# EXERCISE 2.6

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
        print(f"{i} ---> {multi(lista)}")






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