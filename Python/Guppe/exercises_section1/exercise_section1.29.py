"""
Program that reads four grades and calculates the arithmetic mean of them
"""
grade1 = float(input("Type the first grade:"))
grade2 = float(input("Type the second grade:"))
grade3 = float(input("Type the third grade:"))
grade4 = float(input("Type the fourth grade:"))
mean = ((grade1 + grade2 + grade3 + grade4) / 4)
print("The arithmetic mean is: ", mean, "!")
