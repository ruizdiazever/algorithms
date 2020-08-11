import math





# EXERCISE 1.1

class Intro:
    """ This program asks your name and greets you """
    def greeting(self):
        name = input(f"Whats is your name? ")
        print(f"Welcome {name} to the Matrix.")

    """ This function can multiply two numbers """
    def multiplication(self):
        print(f"Please enter 2 numbers.")

        try:
            a = float(input("1. Enter a number: "))
            b = float(input("2. Enter a number: "))
        except:
            print("Error, you have to enter a number.")
        else:
            print(f"3. Result: {int(a * b)}") 





# EXERCISE 1.2

class Geometry:
    # Point A and B
    def rectangle(self, base, altura):
        """ Calculates the perimeter and area of a rectangle given its base and height """
        self.base = base
        self.altura = altura
        print(f"Rectangulo con base {base} y altura {altura}")
        print(f"a) Perimetro: {2 * (base + altura)}")
        print(f"b) Area: {base * altura}")

    # Point D and E
    def circle(self, radio):
        """ Calculates the perimeter and area of a circle given its radius """
        self.radio = radio
        print(f"Circulo de radio {radio}")
        print(f"d) Perimetro: {2 * math.pi * radio}")
        print(f"e) Area: {math.pi * (radio ** 2)}")

    # Point F
    def sphere(self, radio):
        """ Calculates the volume of a sphere given its radius """
        self.radio = radio
        print(f"Esfera de radio {radio}")
        print(f"f) Volumen: {(4 * math.pi * (radio **3)) / 3}")       

    # Point G
    def triangle_rectangle(self, cateto_1, cateto_2):
        """ Calculates the hypotenuse of a right triangle given its legs """
        hipotenusa = math.sqrt((cateto_1 **2) + (cateto_2**2))
        print(f"Triangulo rectangulo de catetos {cateto_1} y {cateto_2}")
        print(f"g) Hipotenusa= {hipotenusa}")


# C
class Hard:
    """ Calculates the area of a rectangle (aligned with the x and y axes) given its x1, x2, y1, y2 coordinates. """
    
    def base(self, x1, y1, x2, y2):
        base = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        print(f"The base is: {base}")
        return base

    def height(self, x1, y1, x2, y2):
        height = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        print(f"The height is: {height}")
        return height

    def area(self, base, altura):
        area = base * altura
        print("The area is: ", area)





# EXERCISE 1.3

def iterador():
    """ Multiplicacion de iterador por iterador """
    for i in range(5): 
        print(i * i)

def raiz():
    """ Raiz cuadrada segun iterador """
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
    a = int(input("1. Ingrese un numero: "))
    b = int(input("2. Ingrese un numero: "))

    print(f"""
    La suma de {a} + {b} es {a + b}
    La resta de {a} - {b} es {a -b}
    La multiplicacion de {a} * {b} es {a * b}
    La division de {a} / {b} es {a / b}
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