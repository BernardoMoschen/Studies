"""
Program that reads a number. Positive case, prints the square root of this number.
If negative, it prints the number squared.
"""
import math

num = float(input("Type a number: "))
if num > 0:
    print("\nPositive number!")
    print("His square root is:", math.sqrt(num))
else:
    print("\nNegative number!")
    print("His value squared is:", math.pow(num, 2))
