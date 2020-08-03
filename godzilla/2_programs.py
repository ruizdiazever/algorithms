# EXERCISE 2.1

def credit():
    coin = float(input("Ingrese la cantidad de euros: "))
    interest = float(input("Introduzca la tasa de interes: "))
    years = int(input("Ingrese la cantidad de años: "))

    final_coin = coin * (1 + ((interest / 100) ** years))

    print(f"El monton final a pagar es: {final_coin}")




# EXCERCISE 2.2

def algorithm():
    num = float(input("Introduzca la tempera en Fahrenheit: "))
    celsius = (num - 32) * 5/9

    print(f"La temperatura de {num} Fahrenheit es {celsius} Celsius.")

test = algorithm()

