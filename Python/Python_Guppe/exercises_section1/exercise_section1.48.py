"""
Program that reads a time in seconds and prints it in hours, minutes and seconds
- without "datetime." (lib)
"""
time = int(input('Enter a time in seconds: '))
hs = 3600
h = int(time / hs)
m = int((time - (h * hs)) / 60)
s = int((time - (h * hs) - (m * 60)))

print(f"The hours is: {h}:{m}:{s}.")
