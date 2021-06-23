""""
Program that calculates the amount to be paid to an employee for the hours worked, granting a increase
"""
hours = float(input("Type the number of hours worked: "))
pricePerHour = float(input("Type the amount($) to be paid for each hour worked:"))
increase = float(input("Type the increase(%) on this amount:"))

print("\nAmount without increased: ", hours * pricePerHour)
print("Increase applied to the amount: ", (increase * (hours * pricePerHour) / 100))
print("\nThe total amount to be paid to the worker is: ",
      hours * pricePerHour + (increase * (hours * pricePerHour) / 100))
