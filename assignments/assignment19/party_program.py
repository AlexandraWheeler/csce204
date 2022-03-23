# Author: Alexandra Wheeler
# Guest List

def getBoolean(item):
    if item == "true":
        return True
    else:
        return False

def getGuests():
    with open("assignments/assignment19/guest_list.txt") as file:
        guestList = {}
        for line in file:
            data = line.split(",")
            name = data[0].lower().strip().capitalize()
            invite = data[1].lower().strip()
            guestList[name] = getBoolean(invite)
        return guestList

def displayGuests(guestList, coming):
    for guest in guestList:
        if guestList[guest] == coming:
            attending.append(guest)
        elif guestList[guest] != coming:
            notAttending.append(guest)

      
print("Guest List for my Party!")
guestList = getGuests()
attending = []
notAttending = []
while True:
    command = input("View (A)ttending, (N)ot Attending, or (Q)uit:  ").strip().lower()
    if command == "q":
        break
    elif command == "a":
        displayGuests(guestList, True)
        print("These guests are attending: ")
        for guest in attending:
            print(f"-{guest}")
    elif command == "n":
        displayGuests(guestList, True)
        print("These guests are not attending: ")
        for guest in notAttending:
            print(f"-{guest}")
    else:
        print("Invalid Command")

print("Goodbye")










getGuests()

