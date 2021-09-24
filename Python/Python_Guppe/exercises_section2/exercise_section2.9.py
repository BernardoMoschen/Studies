"""
Program that reads the worker's salary and the value of the provision of a loan
- If the loan installment value is greater than 20% of the salary, it prints that the loan was not granted.
- Otherwise, it prints that the loan was granted.
"""

salary = float(input("Type the amount($) of the salary: "))
installmentValue = float(input("Type the amount($) of the installment: "))

if (installmentValue / salary * 100) >= 20:
    print("Loan not granted.")
else:
    print("Loan granted.")
