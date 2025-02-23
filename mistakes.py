def add_numbers(x, y):
    result = x + y
    print("Result: " + result)  # TypeError: Cannot concatenate str and int
    return result

def divide(a, b):
    if b == 0:
        print("Can't divide by zero")  # Error, doesn't handle ZeroDivisionError
    else:
        return a // b  # Integer division instead of float division

x = "100"
y = 200
add_numbers(x, y)  # Mixing string and integer will cause errors

z = 15
w = 0
divide(z, w)  # Will not properly handle zero division error

if 5 = 5:  # SyntaxError: Invalid syntax
    print("Equal!") 

def multiply(x, y, z=2):  # Too many arguments passed in the next line
    return x * y

multiply(5, 3, 4, 5)  # TypeError: multiply() takes from 2 to 3 positional arguments

def check_number(num):
    if num > 10  # SyntaxError: Expected an indented block
    print("Greater than 10")
    
check_number(20)

import math
math.acos(1000)  # math domain error, invalid input for acos

x = 50
y = "not a number"
z = x + y  # TypeError: can’t add str to int

def greet(name):
    print("Hello, " + name)
    
greet(123)  # TypeError: can't concatenate str and int
