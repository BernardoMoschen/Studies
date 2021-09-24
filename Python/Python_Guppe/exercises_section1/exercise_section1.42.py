"""
Program that reads a base salary, grants a bonus and discounts the income tax rate
"""

baseSalary = float(input("Type the base salary: "))
bonus = float(input("Type the bonus(%): "))
tax = float(input("Type the tax(%): "))

bonus = bonus * baseSalary / 100
tax = tax * baseSalary / 100

print("\nThe bonus to be paid is: ", bonus, "\nThe tax to be paid is: ", tax)
print("\nThe The value of the final salary is:", baseSalary + bonus - tax)
