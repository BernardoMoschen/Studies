"""
Program that calculates the amount to be paid to an employee for the days worked, discounting income tax
"""
days = float(input("Type the number of days worked: "))
pricePerDay = float(input("Type the amount($) to be paid for each day worked:"))
tax = float(input("Type the rate levied(%) on this amount:"))

print("\nAmount without tax :", days * pricePerDay)
print("Discounted income tax: ", (tax * (days * pricePerDay) / 100))
print("\nThe total amount to be paid to the worker is: ", days * pricePerDay - (tax * (days * pricePerDay) / 100))
