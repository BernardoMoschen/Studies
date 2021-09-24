"""
Program that reads the height and radius of a circular cylinder and prints its volume.
"""
import math

height = float(input("Type the value of the height: "))
radius = float(input("Type the value of the radius: "))

print(f"The volume of the cylinder is: ", math.pi * math.pow(radius, 2) * height)
