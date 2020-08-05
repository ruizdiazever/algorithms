# EXERCISE 2.1

def credit():
    coin = float(input("Ingrese la cantidad de euros: "))
    interest = float(input("Introduzca la tasa de interes: "))
    years = int(input("Ingrese la cantidad de años: "))

    final_coin = coin * (1 + ((interest / 100) ** years))

    print(f"El monton final a pagar es: {final_coin}")




# EXERCISE 2.2

# Toma una temperatura en Fahrenheit y retorna en Celsius y viceversa.
class Temperature:
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


# Instance
test = Temperature()

# Fahrenheit to Celsius
celsius = test.fahrenheit_to_celsius(24)
# Celsius to Fahrenheit
fahrenheit = test.celsius_to_fahrenheit(celsius)
# Result
print(f"{celsius} °C son {fahrenheit} °F")




# EXERCISE 2.3

# Devuelve valores en Celsius de 0 a 120 Fahrenheit con una franja de 10 grados F°.
for i in range (0, 120, 10):
    print(f"{i} Fahrenheit = {test.fahrenheit_to_celsius(i)} Celsius.")
    