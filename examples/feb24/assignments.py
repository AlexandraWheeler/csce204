from datetime import time

assignments = {
    "Assignment 1" : time(9, 45),
    "Assignment 2" : time(10,30),
    "Assignment 3" : time(15,30),
    "Midterm": time(23,59)
}
for assignment in assignments:
    myTime = assignments[assignment]
    print(f"{assignment} is due at {myTime.strftime('%I:%M %p')}")