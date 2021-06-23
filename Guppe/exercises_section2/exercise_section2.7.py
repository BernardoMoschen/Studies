"""
Program that reads two integers and:
- Prints the largest of them.
- Prints the difference between them.
- If by chance they are equal, inform the user.
"""
num1 = int(input("Type a number(integer) :"))
num2 = int(input("Type a second one:"))
if num1 > num2:
    print("\nThe biggest of them is: ", num1)
    print(f"The difference between {num1} and {num2} is: ", num1 - num2)
elif num2 > num1:
    print("\nThe biggest of them is: ", num2)
    print(f"The difference between {num2} and {num1} is: ", num2 - num1)
elif num1 == num2:
    print("\nBoth numbers are equal.")
else:
    print("\nInvalid number typed.")
