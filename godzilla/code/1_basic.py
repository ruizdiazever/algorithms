import math

# EXERCISE 1.1

class Intro:
    def greeting(self):
        name = input(f"Whats is your name? ")
        print(f"Welcome {name}")
    
    def producto(self):
        print(f"Please enter 2 numbers.")

        try:
            num_1 = float(input("1. Enter a number: "))
            num_2 = float(input("2. Enter a number: "))
        except:
            print("Error, you have to enter a number.")
        else:
            print(f"3. Result: {int(num_1 * num_2)}") 





# EXERCISE 1.2

class Geometria:
    # A and B
    def rectangulo(self, base, altura):
        self.base = base
        self.altura = altura
        print(f"Rectangulo con base {base} y altura {altura}")
        print(f"a) Perimetro: {2 * (base + altura)}")
        print(f"b) Area: {base * altura}")

    # D and E
    def circulo(self, radio):
        self.radio = radio
        print(f"Circulo de radio {radio}")
        print(f"d) Perimetro: {2 * math.pi * radio}")
        print(f"e) Area: {math.pi * (radio ** 2)}")

    # F
    def esfera(self, radio):
        self.radio = radio
        print(f"Esfera de radio {radio}")
        print(f"f) Volumen: {(4 * math.pi * (radio **3)) / 3}")       

    # G
    def triangulo_rectangulo(self, cateto_1, cateto_2):
        hipotenusa = math.sqrt((cateto_1 **2) + (cateto_2**2))
        print(f"Triangulo rectangulo de catetos {cateto_1} y {cateto_2}")
        print(f"g) Hipotenusa= {hipotenusa}")


# C
class Hard:
    def base(self, x1, y1, x2, y2):
        base = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        print(f"La base es: {base}")
        return base

    def altura(self, x1, y1, x2, y2):
        altura = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        print(f"La altura es: {altura}")
        return altura

    def area(self, base, altura):
        area = base * altura
        print("El area es: ", area)





# EXERCISE 1.3

def iterador():
    # Multiplicacion de iterador por iterador
    for i in range(5): 
        print(i * i)

def raiz():
    # Raiz cuadrada segun iterador
    for i in range(2, 6): 
        print(i, 2 **i)





# EXERCISE 1.4

def factorial(num):
    if num > 0:
        num = num * factorial(num - 1)
    else:
        num = 1
    return num





# EXERCISE 1.5

def mate():
    num_1 = int(input("1. Ingrese un numero: "))
    num_2 = int(input("2. Ingrese un numero: "))

    print(f"""
    La suma de {num_1} + {num_2} es {num_1 + num_2}
    La resta de {num_1} - {num_2} es {num_1 -num_2}
    La multiplicacion de {num_1} * {num_2} es {num_1 * num_2}
    La division de {num_1} / {num_2} es {num_1 / num_2}
    """)

# Tabla de multiplicar
def multi():
    num = int(input("Ingrese un para saber su tabla de multiplicar: "))

    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")





# EXERCISE 1.6

def quilombo():
    name = input("Whats is your name? ")
    
    for i in range (1001):
        print(name, end=" ")