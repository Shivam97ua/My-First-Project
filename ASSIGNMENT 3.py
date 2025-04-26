# Task 1: Calculate Factorial Using a Function
b=int(input('Enter a Number :'))

def a(b):
    if b<2:
        return 1
    else:
        return b * (a(b-1))
result=a(b)

print("Factorial of",b, "is :", result)
print ('Thank You')


# Task 2: Using the Math Module for Calculations
x=int(input('Enter a Number :'))
import math
print("Square Root : ",math.sqrt(x))
print("logarithm : ",math.log(x))
print("Sine : ",math.sin(x))
print ('Thank You')