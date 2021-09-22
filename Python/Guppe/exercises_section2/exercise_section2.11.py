"""
Program that reads a number, and:
- If the value is greater than 0, it prints the sum of all its numbers.
- If less than 0, it prints that the value entered is invalid.
"""

num = input("Type a number: ")
if int(num) > 0:
    print(sum(int(i) for i in num))
elif int(num) < 0:
    print("You typed an invalid value.")
