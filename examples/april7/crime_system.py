from tkinter import getboolean
from criminal import Criminal

def getCriminals():
    criminals = []
    with open("examples/oop/criminals.txt") as file:
        for line in file:
            data = line.split(",")
            firstName = data[0].strip()
            lastName = data[1].strip()
            gender = data[2].strip().lower()
            crimeType = data[3].strip().lower()
            inJail = get_bool(data[4].strip())
            description = data[5].strip()
            criminals.append(Criminal(firstName, lastName,gender, crimeType, inJail, description))
    return criminals

def get_bool(data):
    if data.lower() == "true":
        return True
    else:
        return False

criminals = getCriminals()

print("Welcome to our Criminal System")
while True:
    command = input("Would you like to: (V)iew, (S)earch, or (Q)uit: ").strip().lower()

    if command == "q":
        break
    elif command == "v":
        for criminal in criminals:
            criminal.display()
    elif command == "s":
        gender = input("Enter 'male' or 'female': ").strip().lower()
        crimeType = input("Enter 'robbery', 'assault', or 'murder': ").strip().lower()

        print("Criminals that match your criteria:")
        for criminal in criminals:
            if criminal.isMatch(gender,crimeType):
                criminal.display()

    else: 
        print("Invalid Command")
