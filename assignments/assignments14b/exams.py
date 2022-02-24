from datetime import date, time, datetime

exams = {
    "CSCE 204": datetime(2022, 2, 24, 8, 30),
    "ITEC 245": datetime(2022, 3, 14, 13, 15),
    "ITEC 370": datetime(2022, 4, 4, 15, 30),
    "CSCE 304": datetime(2022, 3, 23, 10, 45),
    "BIOL 206": datetime(2022, 2, 24, 16, 5), 
    "SPTE 240": datetime(2022, 2, 28, 8, 5),
    "ITEC 265": datetime(2022, 3, 1, 13, 45)
}

today = []
upcoming = []

for exam in exams:
    examTime = exams[exam].strftime(("%I:%M %p"))
    examDate = exams[exam]
    examList = f"{examTime} {exam}"
    if datetime.today().date() == examDate.date():
        today.append(examList)
    elif datetime.today().date() < examDate.date():
        upcoming.append(examList)

print("Todays Exams: ")
for exam in today:
    print(exam)
print("")
print("Upcoming Exams:")
for exam in upcoming:
    print(exam)
