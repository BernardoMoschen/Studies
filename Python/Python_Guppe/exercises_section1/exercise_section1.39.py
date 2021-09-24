"""
Program that divides a value between three individuals
"""

value = float(input("Type the value to be divided: "))
individual1 = float(input("Type the amount(%) to be received by the first one: "))
individual2 = float(input("Type the amount(%) to be received by the second one: "))
print("The third individual receives what is left.")

print("\nThe first one received: ", individual1 * value / 100, "\nThe second one received: ", individual2 * value / 100)
print("The third once received: ", value - (((individual1 * value) / 100) + (individual2 * value) / 100))
