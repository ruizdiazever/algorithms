#  EXERCISE 1.5, basic math and table product.

def mate():
    a = int(input("1. Ingrese un numero: "))
    b = int(input("2. Ingrese un numero: "))

    print(f"""
    La suma de {a} + {b} es {a + b}
    La resta de {a} - {b} es {a -b}
    La multiplicacion de {a} * {b} es {a * b}
    La division de {a} / {b} es {a / b}
    """)

def tableProduct():
    num = int(input("Ingrese un para saber su tabla de multiplicar: "))

    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")