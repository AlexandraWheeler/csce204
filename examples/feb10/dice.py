# Rolling Dice Game
import random
print("Rolling Dice Game")



while True:
    if input("Do you want to roll? (Y or N) ").lower().strip() != "y":
        break
    print(random.randint(1,6))

print("Goodbye")

