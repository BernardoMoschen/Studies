"""
Program that reads a number and case is positive, shows its square root.
If negative, prints that the number is invalid.
(using if)
"""
import math

num = float(input("Type a number: "))
if num > 0:
    print("\nPositive number!")
    print("The square root of the number is: ", math.sqrt(num))
else:
    print("\nYou typed an invalid / negative number.")
