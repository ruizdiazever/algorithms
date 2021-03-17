#  EXERCISE 1.1

class Intro:    
    def greeting(self):
        """ This method asks your name and greets you """
        name = input(f"Whats is your name? ")
        print(f"Welcome {name} to the Matrix.")

    def multiplication(self):
        """ This method can multiply two numbers """
        print(f"Please enter 2 numbers.")

        try:
            a = float(input("1. Enter a number: "))
            b = float(input("2. Enter a number: "))
        except:
            print("Error, you have to enter a number.")
        else:
            print(f"3. Result: {int(a * b)}") 

# Instance of the classs
test = Intro()

# Instance of de function in object
test.greeting()
test.multiplication()