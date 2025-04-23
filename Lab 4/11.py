import math

def degtrad(degrees):
    return degrees * (3.14159 / 180)

def sinTaylor(Rad, terms=10):
    result = 0
    for n in range(terms):
        sign = (-1)**n
        term = (Rad**(2*n + 1)) / math.factorial(2*n + 1)
        result += sign * term
    return result

degrees = float(input("Enter angle in degrees: "))
Rad = degtrad(degrees)
value = sinTaylor(Rad)
print("sin of ",degrees," is : ",value)