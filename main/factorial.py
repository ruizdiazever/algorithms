#  EXERCISE 1.4

def factorial(num):
    if num > 0:
        num = num * factorial(num - 1)
    else:
        num = 1
    return num