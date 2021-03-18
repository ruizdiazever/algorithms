#  EXERCISE 1.6, print your name * 1000

def names():
    name = input("Whats is your name? ")
    
    for i in range (1001):
        print(name, end=" ")

test = names()