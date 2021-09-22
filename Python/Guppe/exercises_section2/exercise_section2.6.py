"""
Program that reads two entire numbers and:
- Prints the largest of them.
- Prints the difference between them.
"""

num1 = int(input("Type a number(integer) :"))
num2 = int(input("Type a second one:"))

if num1 > num2:
    print("\nThe biggest of them is: ", num1)
    print(f"The difference between {num1} and {num2} is: ", num1 - num2)
else:
    print("\nThe biggest of them is: ", num2)
    print(f"The difference between {num2} and {num1} is: ", num2 - num1)
