import random

def roll():
    return random.randint(1,6)

print("Lets decide who goes first")

player1roll1 = roll()
player1roll2 = roll()
player1total = player1roll1 + player1roll2

player2roll1 = roll()
player2roll2 = roll()
player2total = player2roll1 + player2roll2

print(f"Player 1 rolls {player1roll1} and {player1roll2} = {player1total}")
print(f"Player 2 rolls {player2roll1} and {player2roll2} = {player2total}")

if player1total>player2total:
    print("Player 1 goes first.")
elif player2total > player1total:
    print("Player 2 goes first.")
else:
    print("Tie")