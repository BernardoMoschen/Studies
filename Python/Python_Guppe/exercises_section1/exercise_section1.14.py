"""
Program that reads a value (angle) in degrees and converts it to radians
"""
import math
degrees = float(input('Type the value of degrees:'))
print(f'The value of {degrees} angle degrees converted to radians is: ', degrees * (math.pi/180), ' .')
