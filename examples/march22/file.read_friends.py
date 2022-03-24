def getFriends():
    friends = []

    with open("examples/march22/friends.txt") as file:
        for line in file:
            friends.append(line.strip())
        return friends

people = getFriends()

print("Party Time")

while True:
    userInput = input("(C)heck Guest, (L)ist Guest, (Q)uit: ").strip().lower()
    if userInput == "c":
        name = input("Enter name: ").strip().lower().capitalize()
        if name in people:
            print("Welcome")
        else: 
            print("Sorry, you are not invited. ")
    elif userInput == "l":
        print("Friends: ")
        for person in people:       
            print(person)
    elif userInput == "q":
        break
    else:
        print("Invalid Command")
