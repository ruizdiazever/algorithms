# EXERCISE 2.3
from . import temperature
test = temperature()


def temperature_table_10():
    """ Devuelve valores en Celsius de 0 a 120 Fahrenheit con una franja de 10 grados F°. """
    for i in range (0, 120, 10):
        print(f"{i} Fahrenheit = {test.fahrenheit_to_celsius(i)} Celsius.")