"""
Program that calculates how many steps will be necessary to climb a ladder,
based on the reading of the step height and the total height to be reached.
"""

totalHeight = float(input("Type the total height: "))
stepHeight = float(input("Type the step height: "))

print("\nThe required number of steps to climb is:", totalHeight / stepHeight)
