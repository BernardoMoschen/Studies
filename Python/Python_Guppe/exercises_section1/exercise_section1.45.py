"""
Program to convert string to lowercase
"""
string = input("Type the string: ")
string1 = ''

for i in string:
    if 65 <= ord(i) <= 90:
        string1 = string1 + chr((ord(i) + 32))
    else:
        string1 = string1 + i

print("\nOriginal string in uppercase  =  ", string)
print("The original string in lowercase =  ", string1)
