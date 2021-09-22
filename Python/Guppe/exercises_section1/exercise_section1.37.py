"""
Program to calculate the discount on a product
"""
discount = float(input("Type the discount amount: "))
price = float(input("Type the price of the product: "))

print("The final price is: ", price - ((discount * price) / 100))