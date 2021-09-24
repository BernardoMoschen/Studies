"""
Program to share an amount of profit, based on the amount invested by each of up to three participants:
"""
profit = float(input("Type the value of the profit: "))
amount1 = float(input("Type the amount(%) invested by the first participant: "))
amount2 = float(input("Type the amount(%) invested by the second: "))
amount3 = float(input("Type the amount(%) invested by the third: "))

profit1 = amount1 * profit / 100
profit2 = amount2 * profit / 100
profit3 = amount3 * profit / 100

print("\nThe amount divided between the 3 participants results in:")
print(f"For the first participant: {profit1} \nFor the second: {profit2} \nAnd for the last one: {profit3}")
