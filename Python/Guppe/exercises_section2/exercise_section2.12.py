"""
Program that reads a number, and:
- If the value is positive, it prints gis logarithm.
- If negative, it prints that the value entered is invalid.
"""
import math

num = float(input("Type a number: "))

if num > 0:
    print("His logarithm is: ", math.log(num))
else:
    print("You typed an invalid value.")
