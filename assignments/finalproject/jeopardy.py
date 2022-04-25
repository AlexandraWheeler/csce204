# Author: Alexandra Wheeler
# Jeopardy
# get question holds the title of that question
from question import Question
import random
import turtle
pen = turtle.Turtle()
style = ("Courier", 20, "normal")
style2 = (("Courier", 30, "normal"))

def getQuestions():
    questions = []
    try:
        with open("assignments/finalproject/questions.txt") as file:
            for line in file:
                data = line.split(",")
                question = data[0].strip()
                answer = data[1].strip()
                questions.append(Question(question,answer))
    except FileNotFoundError:
        print("File Cannot Be Found")
    return questions

def displayQuestion(question):
    setPos(-200,50)
    pen.write(question.getQuestion(), font = style)

def displayAnswer(question):
    answer = question.getAnswer()
    return answer



def displayUnderscore(question):
    #pen.write(question.getAnswer())
    setPos(-100,-50)
    #question = question.getAnswer()
    underscoreWord = ""
    for i in range(len(question)):
        underscoreWord += "_"
    #pen.write(underscoreWord, font = style2)
    return underscoreWord

def displayWord(word):
    displayWord = " "
    setPos(-125,-50)
    for i in range(len(word)):
        displayWord += word[i] + " "
    pen.write(displayWord, font = style2)

def setPos(x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()

def checkAnswer(answer,letter):
    for i in answer:
        if i.lower() == letter.lower():
            return True
    return False

def displayIncorrect():
    setPos(-125,-100)
    pen.write("Incorrect Letters:", font = style)

def addIncorrect(letter,x,y):
    setPos(x,y)
    pen.write(letter, font=style)


def guessLetter(x,y):
    global question
    global answer
    global guessedWord
    global wrongAttemptnum
    newGuessedWord = ""
    wrongPossibility = 0
    outcome = 0
    x = -200
    y = -125
    incorrectLetters = []
    letter = turtle.textinput("Letter Guessing", "Enter a Letter: ")
    for i in range(len(answer)):
        if answer[i] == letter:
            newGuessedWord += letter
        else:
            newGuessedWord += guessedWord[i]
    for i in range(len(answer)):
        if answer[i] != letter:
            wrongPossibility += 1
            incorrectLetters.append(letter)
            addIncorrect(incorrectLetters[0],x,y)
            incorrectLetters.clear()
        else:
            continue
        

        

        



questionList = getQuestions()
question = random.choice(questionList)
answer = displayAnswer(question)

displayQuestion(question)
guessedWord = displayUnderscore(answer)
displayWord(guessedWord)
displayIncorrect()

x = 0
y = 0
wrongAttemptnum = 0

guessLetter(0,0)








turtle.done()




    




