#  EXERCISE 1.4, factorial of a number.

def factorial(num):
    if num > 0:
        num = num * factorial(num - 1)
    else:
        num = 1
    return num