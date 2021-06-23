"""
Program that reads 3 grades and calculates the weighted average between them,
if the result is greater than 5.0, it prints that the student has passed,
if it is from 3 to 4.9 he is in recovery, otherwise it prints that he has failed.
"""

print("First type the grade for the Lab Work (weight 2):")
labGrade = float(input("Type the grade: "))
print("\nNow, type the grade for the Semiannual Assessment(weight 3): ")
semiannualGrade = float(input("Type the grade: "))
print("\nFinally, enter the grade of the Final Exam (weight 5): ")
examGrade = float(input("Type the grade: "))

average = (labGrade * 2 + semiannualGrade * 3 + examGrade * 5) / (2 + 3 + 5)
if average >= 5.0:
    print("The student has passed !")
elif 4.9 <= average >= 3.0:
    print("Summer School.")
else:
    print("The student failed")
print(f"His final grade is : {average}.")
