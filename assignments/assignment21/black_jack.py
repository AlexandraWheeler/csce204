# Author: Alexandra Wheeler
# Playing Black Jack
import random
import string

def getScore():
    with open("assignments/assignment21/score.txt") as file:
        lines = file.readlines()
        if not lines: 
            return 0
        return int(lines.pop().strip())
       

def saveScore(score):
    with open("assignments/assignment21/score.txt", "w") as file:
        file.write(f"{score}\n")

def userHand():
    
    return userHand



def playRound():
    userCard1 = random.randint(1,11)
    userCard2 = random.randint(1,11)
    userHand = userCard1 + userCard2
    print(f"Your hand total: {userHand}")
    while True:
        userInput = input("Do you want to draw another card? (Y)es or (N)o: ").strip().lower()
        if userInput == "n":
            break

        elif userInput == "y":
            card = random.randint(1,11)
            print(f"You drew a {card}")
            userHand += card
            print(f"Your hand totals {userHand}")
        
        else:
            print("invalid command")

    computerHand = random.randint(14,23)  
    print(f"Computer's hand total: {computerHand}")  
    if computerHand > userHand:
        print("\nYou win")
        return 1
    elif computerHand < userHand:
        print("\nYou lose")
        return -1
    else:
        return 0           

            



print("Welcome to Black Jack!")
score = getScore()
computerHand = random.randint(14,23)
while True:
    command = input("Do you want to (P)lay or (Q)uit? ").strip().lower()
    if command == "q":
        break
    elif command != "p":
        print("Invalid Command")
        continue
    if command == "p":
        roundScore = playRound()
        score += roundScore

print(f"Your current score is {score}.")

saveScore(score)
print("Goodbye")

        
        



    
