"""
Program that reads two grades, and:
- Check if they are valid
- If valid, calculate the average.
- If invalid, the user is informed and the program is closed.
"""

grade1 = float(input("Type the first grade: "))
grade2 = float(input("Type the second one: "))
if 0.0 <= grade1 <= 10.0 and 0.0 <= grade2 <= 10.0:
    print("\nThe average is:", grade1 + grade2 / 2)
else:
    print("\nThe informed grades are invalid.")
