"""
Program that reads three values and presents the result of the sum of these values squared.
"""
import math
print("Type the tree values you want to calculate")
value1 = float(input("Type the first value: "))
value2 = float(input("Type the second value: "))
value3 = float(input("Type the third value :"))
soma = ((math.pow(value1, 2)) + (math.pow(value2, 2) + math.pow(value3, 2)))
print("\nThe result is:", soma, " !")
