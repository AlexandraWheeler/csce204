#Author: Alexandra Wheeler

# input grades
print("Lets calculate your grade")
assignments = float(input("What was your average grade for your assignments? "))
exercises = float(input("What was your average grade for your exercises? "))
midterm = float(input("What was your grade for your Midterm? "))
final = float(input("What was your grade for your Final Exam? "))

letterGrade = ""

finalGrade = assignments * .5 + exercises * .2 + midterm * .15 + final * .15

print(f"Your final grade will be {round(finalGrade, 2)}. ")

if finalGrade >= 90: 
    letterGrade = "A"
elif finalGrade >= 80:
    letterGrade = "B"
elif finalGrade >= 70:
    letterGrade = "C"
elif finalGrade >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"

print(f"Letter Grade: {letterGrade}")