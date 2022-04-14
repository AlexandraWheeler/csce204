def displayLetters(word):
    for i in range(len(word)):
        print(word[i])

#displayLetters("happy")

def starWord(word):
    print("*", end = "")
    for letter in word:
        print(letter + "*", end = "")

#starWord("happy")

def inWord(word,letter):
    for l in word:
        if l == letter:
            return True
        
    return False

if inWord("happy", "h"):
    print("Yay")
else:
    print("no")