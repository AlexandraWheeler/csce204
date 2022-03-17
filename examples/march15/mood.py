def good_mood(color):
    mood_chart = {
        "red":"angry",
        "yellow":"happy",
        "blue":"sad",
        "green":"sick",
        "purple":"nervous",
        "black":"scared",
        "pink":"excited"
    }
    color = color.strip().lower()

    if color in mood_chart:
        return mood_chart[color]
    else:
        return "confused"

print(good_mood("pink"))