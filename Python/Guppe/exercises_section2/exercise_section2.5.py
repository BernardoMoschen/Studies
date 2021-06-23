"""
Program that reads an integer and verifies whether it is even or odd
"""

num = int(input("Type a number(integer): "))
if num % 2 == 0:
    print(f"\nThe number {num} is even !")
else:
    print(f"\nThe number {num} is odd !")
