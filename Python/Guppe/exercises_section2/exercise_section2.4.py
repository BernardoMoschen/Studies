"""
Program that reads a number and, if positive:
- Prints the number squared.
- Prints his square root.
"""

import math

num = float(input("Type a number: "))
if num > 0:
    print("\nHis value squared is: ", math.pow(num, 2))
    print("His square root is: ", math.sqrt(num))
