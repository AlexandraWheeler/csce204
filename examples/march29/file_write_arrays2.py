
from webbrowser import get


def getFriends():
    friends = []
    with open("examples/march29/friends.txt") as file:
        for line in file:
            friends.append
    return friends

def writeFriends(friends):
    with open("examples/march29/friends.txt", "w") as file:
        for friend in friends:
            file.write(f"{friend}\n")

def displayFriends(friends):
    for friends in friends:
        print(f"-{friend}")

# read list
friendList = getFriends()


# modify list
print("Hey Friends!")
while True:
    command = input("(A)dd, (D)elete, (V)iew, (Q)uit: ").lower().strip()
    if command == "q":
        break
    elif command == "a":
        name = input("Enter friend name: ")
        friendList.append(name)
        print(f"{name} was added to the list.")
    elif command == "v":
        displayFriends(friendList)

print("Goodbye")



# save list
writeFriends(friendList)
