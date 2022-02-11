# Author: Alexandra Wheeler
# List of Debts

debtName = []
debtAmount = []

print("Here are your debts:")
while True:
    answer = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").lower()
    if answer == "v":
        for i in range(len(debtName)):
            print(f"-{debtName[i]}: {debtAmount[i]}")
    elif answer == "a":
        name = input("Enter debt name: ")
        debtName.append(name)
        amount = input("Enter debt amount: ")
        debtAmount.append(amount)
    elif answer == "r":
        print("You cannot remove debt!")
    elif answer == "q":
        break
    else:
        print("Invalid Command")

print("Goodbye")
        