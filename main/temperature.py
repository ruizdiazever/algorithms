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