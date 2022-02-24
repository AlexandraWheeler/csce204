from datetime import date

birthdays = {
    "Amy" : date(2023, 1, 22),
    "Rob" : date(2022, 3, 4),
    "Carl" : date(2023, 4 , 5)
}

for friend in birthdays:
    daysUntil = (birthdays[friend] - date.today()).days
    print(f"{friend} - {daysUntil} days away.")
