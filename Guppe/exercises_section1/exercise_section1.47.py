"""
Program that reads an integer and prints each one of the digits, separately
- without "datetime." (lib)
"""

num = int(input("Type a number:"))
p = str(num)
u = num // 1 % 10
t = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"\nVerifying your number...")
print(f"The unit is: ", u)
print(f"The ten is: ", t)
print(f"The hundred is: ", c)
print(f"The thousands are: ", m)
