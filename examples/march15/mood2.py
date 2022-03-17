def good_mood(color):
    if color == "red":
        return "angry"
    elif color == "blue":
        return "sad"
    elif color == "purple":
        return "nervous"
    elif color == "green":
        return "nervous"
    elif color == "yellow":
        return "happy"
    elif color == "pink":
        return "excited"
    else:
        return "confused"

    

print("Mood Ring!!")

while True:
    color = input("Enter color: ").strip().lower()
    mood = good_mood(color)
    print(f"You are feeling {mood}")
    command = input("Play Again: (Y)es or (N)o? ").strip().lower()
    if command != "y" and command != "yes":
        break
print("Goodbye")