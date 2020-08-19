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

    a = timeToSeconds()
    b = timeToSeconds()

    time = a + b

    solution = secondsToTime(time)