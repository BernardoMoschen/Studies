"""
Program to calculate and inform the ideal weight, based on the person's height and gender.
"""
gender = input("Type your gender (M or F): ")
height = float(input("Type you height: "))

if gender == 'M':
    print("\nYour ideal weight is: ", (72.7 * height) - 58)
elif gender == "F":
    print("\nYour ideal weight is: ", (62.1 * height) - 44.7)
else:
    print("You typed an invalid value, remember that the gender must be M or F and the height must be a number.")
