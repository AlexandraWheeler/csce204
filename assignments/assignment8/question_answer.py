# Author: Alexandra Wheeler
# Guessing Game
import random

print("Welcome to our Question Answer Game")
num = random.randint(1,3)
again = "y"

while again == "y":
    userQ = input("Ask a yes or no question: ")
    if num == 1:
        print("Yes")
    else:
        print("No")
    again = input("Would you like to ask another question? (Y or N) ").lower().strip()
print("Goodbye!")




