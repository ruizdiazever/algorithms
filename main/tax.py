# EXERCISE 2.1

def credit():
    coin = float(input("Ingrese la cantidad del prestamo en euros: "))
    interest = float(input("Introduzca la tasa de interes: "))
    years = int(input("Ingrese la cantidad de años: "))

    final_coin = coin * (1 + ((interest / 100) ** years))

    print(f"El monton final a pagar es: {final_coin}")