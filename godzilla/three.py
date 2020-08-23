# EXERCISE 3.1

# A
def timeToSeconds():
    "This function return the time in seconds"
    hours = int(input("Hours: "))
    minutes = int(input("Minutes: "))
    seconds = int(input("Seconds: "))

    hours *= 3600
    minutes *= 60
    seconds = seconds + hours + minutes

    return seconds

# B
def secondsToTime(*args):
    "This function return the time in hours, minutes and seconds."

    "Asigno en la variable large la cantidad de de elementos en args."
    large = len(args)

    "Si el large es igual a cero la funcion no tiene argumentos y pide los segundos al usuario."
    if large == 0:
        seconds = int(input("Please input time in seconds: "))
    else:
        for i in range(1):
            seconds = args[i]

    minutes = 0
    hours = 0

    hours = seconds / 3600
    seconds = seconds % 3600

    minutes =   seconds / 60
    seconds = seconds % 60

    print(f"""
    Hours:   {int(hours)}
    Minutes: {int(minutes)}
    Seconds: {int(seconds)}
    """)




# EXERCISE 3.2


class Time:
    "Pide 2 intervalos de tiempo expresados en horas, minutos y segundos usando la funcion 'timeToSeconds()' y sumas los mismos usando la funcion 'timeToSeconds()'"

    def time(self):
        a = timeToSeconds()
        b = timeToSeconds()

        time = a + b

        solution = secondsToTime(time)


# EXERCISE 3.3

def product():
    "Dado cuatro numeros esta funcion devuelve el mayor producto de dos de ellos."
    "Gracias 'deque' podemos sacar el primer elemento en entrar, como una cola."
    from collections import deque

    #  Defino la cola 'numbers'.
    numbers = deque()

    # Creo una tupla para poner los valores y asignarle el producto como clave.
    final = {}
    
    # Itero en la cola e introduzco valores por teclado.
    print("Welcome, please indroducing four number.")
    for i in range(4):
        num = int(input(f"{i+1}. Please input a number: "))
        numbers.append(num)
    
    # De esta manera podemos mutar valores de la cola
    for i in list(numbers):
        for x in list(numbers):
            if (x != i):
                product = i * x
                
                # Uso mi tupla, le asigno como clave el producto y como valor un String
                final[product] = f"{i} * {x} = {product}"
        # Eliminamos por cada salto en i un elemento de la izquierda
        numbers.popleft()

    # Esto devuelve la clave con valor maximo de la tupla
    maximo = max(final)

    # Magic!
    for clave in final:
        if clave == maximo:
            print(final[clave])
