#Author: Alexandra Wheeler

print("Lets calculate your grade")
assignments = float(input("What was your average grade for your assignments? "))
exercises = float(input("What was your average grade for your exercises? "))
midterm = float(input("What was your grade for your Midterm? "))
final = float(input("What was your grade for your Final Exam? "))

classGrade = assignments * .55 + exercises * .15 + midterm * .15 + final * .15
print(f"Your final grade will be {round(classGrade, 2)}. ")