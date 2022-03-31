# Author: Alexandra Wheeler
# Expenses File

FILE_NAME= "assignments/assignment22/expenses.txt"

def readExpenses():
    expenses = {}
    try:
        with open(FILE_NAME) as file:
            for line in file:
                data = line.split(":")
                expense = data[0].lower().strip().capitalize()
                cost = data[1].lower().strip()
                expenses[expense] = int(cost)
    except FileNotFoundError:
        print("Cannot find file.")
    return expenses

def writeExpenses(expenses):
    try:
        with open(FILE_NAME,"w") as file:   
            for expense in expenses:
                file.write(f"{expense}: {expenses[expense]}\n")
            
    except FileNotFoundError:
        print("File not found")

def listExpenses(expenses):
    print("Expenses:")
    for expense in expenses:
        print(f"{expense}: ${expenses[expense]}")
    total = 0
    for expense in expenses:
        total += int(expenses[expense])
    with open(FILE_NAME,"w") as file:
        file.write(f"Total: {total}\n")
    print(f"Total: {total}")


def addExpense(expenses):
    expense = input("Expense: ").strip()
    cost = int(input("Cost: "))
    expenses[expense] = cost
    print(f"{expense} was added.")


# main program
expenses = readExpenses()
while True:
    command = input("(A)dd Expense, (L)ist Expenses, or (Q)uit: ").strip().lower()
    if command == "q":
        break
    elif command == "a":
        addExpense(expenses)
    elif command == "l":
        listExpenses(expenses)
    else:
        print("Invalid Command")

print("Goodbye")
writeExpenses(expenses)

