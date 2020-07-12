import math


# Ejercicio 1.1
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


# Exercise 1.2
class Geometria:
    # Exercises A and B
    def rectangulo(self, base, altura):
        self.base = base
        self.altura = altura
        print(f"Rectangulo con base {base} y altura {altura}")
        print(f"a) Perimetro: {2 * (base + altura)}")
        print(f"b) Area: {base * altura}")

    # Exercises D and E
    def circulo(self, radio):
        self.radio = radio
        print(f"Circulo de radio {radio}")
        print(f"d) Perimetro: {2 * math.pi * radio}")
        print(f"e) Area: {math.pi * (radio ** 2)}")

    # Exercise F
    def esfera(self, radio):
        self.radio = radio
        print(f"Esfera de radio {radio}")
        print(f"f) Volumen: {(4 * math.pi * (radio **3)) / 3}")       

    # Exercise G
    def triangulo_rectangulo(self, cateto_1, cateto_2):
        hipotenusa = math.sqrt((cateto_1 **2) + (cateto_2**2))
        print(f"Triangulo rectangulo de catetos {cateto_1} y {cateto_2}")
        print(f"g) Hipotenusa= {hipotenusa}")


# Exercise C
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


# EJECUTION
# Instanciamos
harcore = Hard()
# Base (Vertice de A a B)
b = harcore.base(1,1,4,2)
# Altura (Vertice de B a C)
a = harcore.altura(4,2,6,-4)
# Area
harcore.area(b, a)
