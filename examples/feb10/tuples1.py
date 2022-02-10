weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

#for day in weekdays:
#    print(day)

for i in range(len(weekdays)):
    print(f"{i+1}. {weekdays[i]} ")

count = 1
for day in weekdays:
    print(f"{count}. {day}")
    count += 1