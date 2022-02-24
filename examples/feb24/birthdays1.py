from datetime import date
birthdays = [date(2022,11,1), date(2022,8,14), date(2022,4,4), date(2023,2,6), date(2022,2,25)]

# loop and display bdays
for birthday in birthdays:
    daysAway = (birthday - date.today()).days
    print(f"{birthday.strftime('%b %d')}- Your birthday is {daysAway} days away.")
