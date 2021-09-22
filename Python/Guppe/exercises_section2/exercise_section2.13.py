"""
Program that reads 3 grades and calculates the weighted average between them,
if the result is greater than 60, it prints that the student has passed, otherwise it prints that he has failed.
"""

print("Firstly, the first two notes that have a weight of 1")
grade1 = float(input("Type the first grade: "))
grade2 = float(input("Type the second grade: "))
print("\nNow, the third note, which has a weight of 2.")
grade3 = float(input("Type the third one:"))

average = (grade1 * 1 + grade2 * 1 + grade3 * 2) / (1 + 1 + 2)
if average > 6.0:
    print(f"The student has passed!\nHis final grade is: {average}.")
else:
    print(f"Student failed.\nHis final grade is: {average}.")
