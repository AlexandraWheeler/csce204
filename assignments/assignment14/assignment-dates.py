# Author: Alexandra Wheeler
# Displaying Assignments and Days until due
from datetime import date
assignments = {
    "Assignment 1 - Introduction" : date(2022, 1, 15),
    "Assignment 2 - Book Reading" : date(2022, 1 ,26),
    "Assignment 3 - Homework 1 Questions" : date(2022, 2, 2),
    "Assignment 4 - Quiz One" : date(2022, 2, 14),
    "Assignment 5 - Book Questions" : date(2022, 2, 24),
    "Assignment 6 - Test One" : date(2022, 3, 5),
    "Assignment 7 - Homework 2 Questions" : date(2022, 3 ,17),
    "Assignment 8 - Quiz Two" : date(2022, 3, 31),
    "Assignment 9 - Final Review" : date(2022, 4, 15),
    "Assignment 10 - Final" : date(2022, 4, 28)
}

for assignment in assignments:
    daysUntil = (assignments[assignment] - date.today()).days
    if daysUntil < 0:
        print(f"{assignment} - {abs(daysUntil)} Days Past Due.")
    elif daysUntil == 0:
        print(f"{assignment} - Due Today!")
    elif 0 < daysUntil < 15:
        print(f"{assignment} - Due in {daysUntil} days")
    else:
        dates =  assignments[assignment]
        print(f"{assignment} - {dates.strftime('%b %d, %A')}")
    


