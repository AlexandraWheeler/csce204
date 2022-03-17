import random

def roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    totalDice = dice1 + dice2
    print(f"Dice 1: {dice1}, Dice 2: {dice2}, Total: {totalDice}")
    return totalDice
print("Lets decide who goes first")


print("Player One Rolls:")
player1total = roll()

print("Player Two Rolls:")
player2total = roll()

if player1total>player2total:
    print("Player 1 goes first.")
elif player2total > player1total:
    print("Player 2 goes first.")
else:
    print("Tie")