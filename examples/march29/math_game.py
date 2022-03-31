import random

def getScore():
    with open("examples/march29/score.txt") as file:
        lines = file.readlines()
        if not lines: 
            # if there are no lines in the file
            return 0
        return int(lines.pop().strip())
        # pop takes the first item and takes off white space and returns it

def saveScore(score):
    with open("examples/march29/score.txt", "w") as file:
        file.write(f"{score}\n")

def sumDigits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number = number // 10
    return sum

def playRound():
    randNum = random.randint(1000,9999)
    ans = sumDigits(randNum)

    userAns = int(input(f"Sum of the digits of {randNum}: "))
    if userAns == ans:
        return True
    else: 
        print(f"Incorrect, the answer should be {ans}")
        return False


# read in score
score = getScore()

# play game and modify score
print("Welcome to my Math Game!")
while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()
    if command == "q":
        break
    elif command != "p":
        print("Invalid Command")
        continue 
    if playRound():
        print("Congrats!")
        score += 1

    print(f"Your score is {score}")

               

# save score
saveScore(score)