# Author: Alexandra Wheeler
# Card dealing game
import random

def deal():
    card = random.randint(1,13)
    if card == 1:
        print("Ace")
        return 1
    elif card == 2:
        print("2")
        return 2
    elif card == 3:
        print("3")
        return 3
    elif card == 4:
        print("4")
        return 4
    elif card == 5:
        print("5")
        return 5
    elif card == 6:
        print("6")
        return 6
    elif card == 6:
        print("Ace")
        return 6
    elif card == 7:
        print("7")
        return 7
    elif card == 8:
        print("8")
        return 8
    elif card == 9:
        print("9")
        return 9
    elif card == 10:
        print("10")
        return 10
    elif card == 11:
        print("Jack")
        return 10
    elif card == 12:
        print("Queen")
        return 10
    elif card == 13:
        print("King")
        return 10
    
print("Welcome to my Card Game")
userInput = "y"
computer = 0
user = 0

while True:
    print("The computer deals a: ")
    computerCard = deal()
    print("You deal a: ")
    userCard = deal()

    if computerCard > userCard:
        computer += 1
        print("The computer won this round.")
    elif userCard > computerCard:
        user += 1
        print("You won this round.")
    userInput = input("Do you want to play again? (Y)es or (N)o: ").lower().strip()
    if userInput != "y" and userInput != "yes":
        print(f"""
Your score: {user}
Computer Score: {computer}""")
        if user > computer:
            print("Congrats, You won!")
        elif computer > user:
            print("The computer won")
        else:
            print("Tie!")
        break

print("Goodbye")







