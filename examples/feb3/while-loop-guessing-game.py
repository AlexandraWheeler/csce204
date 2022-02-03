import random

goal = random.randint(1,100)
numGuesses = 1
#print(f"Secret goal is {goal}")

print("Welcome to our guessing game!")
guess= int(input("Enter number between 1 and 100: "))

while guess != goal:
    print(f"Sorry, {guess} is not the answer")
    if guess < goal:
        print(f"{guess} was too low." )
    else:
        print(f"{guess} was too high." )
    guess= int(input("Enter number between 1 and 100: "))
    numGuesses += 1

print(f"You guessed it! The number was {goal}. You got it in {numGuesses} guesses.")