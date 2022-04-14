from ctypes.wintypes import WORD


# using global to access variable in the function *DO NOT USE*
#def replaceStars():
    #global word

    #word = "I am sad"

#word = "I am happy"
#replaceStars()
#print(word)

def replaceStars():
    global word
    answer = ""

    for letter in word:
        if letter == "*":
            answer += "."
        else:
            answer += letter

    word = answer

word = "* happy * I love ****"
replaceStars()
print(word)