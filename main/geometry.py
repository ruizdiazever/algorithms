#  EXERCISE 1.2

import math
class Geometry:
    # A and B
    def rectangle(self, base, altura):
        """ This method calculates the perimeter and area of a rectangle given its base and height """
        self.base = base
        self.altura = altura
        print(f"Rectangulo con base {base} y altura {altura}")
        print(f"a) Perimetro: {2 * (base + altura)}")
        print(f"b) Area: {base * altura}")

    # D and E
    def circle(self, radio):
        """ This method calculates the perimeter and area of a circle given its radius """
        self.radio = radio
        print(f"Circulo de radio {radio}")
        print(f"d) Perimetro: {2 * math.pi * radio}")
        print(f"e) Area: {math.pi * (radio ** 2)}")

    # F
    def sphere(self, radio):
        """ Calculates the volume of a sphere given its radius """
        self.radio = radio
        print(f"Esfera de radio {radio}")
        print(f"f) Volumen: {(4 * math.pi * (radio **3)) / 3}")       

    # G
    def triangle_rectangle(self, cateto_1, cateto_2):
        """ Calculates the hypotenuse of a right triangle given its legs """
        hipotenusa = math.sqrt((cateto_1 **2) + (cateto_2**2))
        print(f"Triangulo rectangulo de catetos {cateto_1} y {cateto_2}")
        print(f"g) Hipotenusa= {hipotenusa}")


#  C
class Hard:
    """ Calculates the area of a rectangle (aligned with the x and y axes) given its x1, x2, y1, y2 coordinates."""
    
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