
def getPhonebook():
    phoneList = {}
    with open("examples/march22/phones.txt") as file:
        for line in file:
            data = line.split(",")
            name = data[0].lower().strip().capitalize()
            number = data[1].lower().strip()
            phoneList[name] = number
    return phoneList

def displayPhonebook(phoneBook):
    for name in phoneBook:
        print(f"{name}: {phoneBook[name]}")

def phoneNumber(phoneBook, name):
    cleanName = name
    if cleanName in phoneBook:
        print(f"{name}'s  number is {phoneBook[cleanName]}")
    else:
        print(f"Sorry, {name} is not in our phone book.")

phoneBook = getPhonebook()

# see if your name is in phone book

while True:
    command = input("(V)iew, (G)et Number, (Q)uit: ").strip().lower()
    if command == "v":
        # display phone book
        displayPhonebook(phoneBook)
    elif command == "g":
        name = input("Enter name: ").lower().capitalize().strip()
        phoneNumber(phoneBook, name)
    elif command == "q":
        break
    else:
        print("Invalid Command")

print("Goodbye")

    