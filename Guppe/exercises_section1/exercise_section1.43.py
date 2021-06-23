"""
Program to help salespeople that reads a total value and prints:
- The total amount to be paid discounted 10% if its in cash.
- The value of each installment, in a 3x installment without interest.
- The seller's commission, if the sale is in cash (5% on the amount already discounted).
- The seller's commission if the sale is in installments (5% of the total amount).
"""

originalValue = float(input("Type the original/initial value: "))
cash = float(originalValue - ((10 * originalValue) / 100))
installment3 = float(originalValue / 3)
cashCommission = float(5 * cash / 100)
installmentCommission = float(5 * originalValue / 100)

print("\nPrice to be paid if the sale is in cash: ", cash)
print("The seller's commission, if the sale is in cash :", cashCommission)

print("\nThe value of each installment, in a 3x installment without interest: ", installment3)
print("The seller's commission if the sale is in installments :", installmentCommission)
