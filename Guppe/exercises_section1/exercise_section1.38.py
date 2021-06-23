"""
Program to read a salary and apply a raise amount on it
"""

salary = float(input("Type the salary: "))
raiseAmount = float(input("Type the raise amount :"))

print("The new salary is: ", salary + (raiseAmount * salary) / 100)

