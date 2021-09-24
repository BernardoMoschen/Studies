"""
Program that calculates the expense needed to surround a land based on its dimensions
"""

length = float(input("Type the length of the land: "))
width = float(input("Type the width of the land: "))
fencePrice = float(input("Type the fence price($): "))

print("\nThe necessary amount to be spent is: ", (length * 2 + width * 2) * fencePrice)
