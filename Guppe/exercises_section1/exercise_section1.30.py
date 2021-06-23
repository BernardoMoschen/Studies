"""
Program that reads a value in Real (R$) and converts it to Dollar (USD)
"""

quotUSD = float(input("Type the Dollar quotation: $ "))
real = float(input("Type the amount of Real: R$ "))
print("The total dollar amount is: $", round(real / quotUSD, 2))
