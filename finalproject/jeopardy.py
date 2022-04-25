# Author: Alexandra Wheeler
# Jeopardy

from question import Question
import random
import turtle
pen = turtle.Turtle()
underline = turtle.Turtle()
turtle.bgcolor("lavender")
pen.pensize(1)
pen.speed(.5)
pen.color("black")
style = ("Courier", 20, "normal")
style2 = (("Courier", 30, "normal"))
style3 = (("Courier", 50, "normal"))

pen.hideturtle()

# retrieves questions from file
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

# turtle displays the question
def displayQuestion(question):
    setPos(-200,50)
    pen.write(question.getQuestion(), font = style)

# turtle returns the answer
def displayAnswer(question):
    answer = question.getAnswer()
    return answer

# returns the underscore version of answer
def displayUnderscore(question):
    setPos(-100,-50)
    underscoreWord = ""
    for i in range(len(question)):
        underscoreWord += "_"
    return underscoreWord

# prints the underscore version of the word
def displayWord(word):
    displayWord = " "
    setPos(-130,-50)
    for i in range(len(word)):
        displayWord += word[i] + " "
    underline.write(displayWord, font = style2)

# sets position
def setPos(x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    underline.up()
    underline.setpos(x,y)
    underline.down()

# checks the answer vs guess
def checkAnswer(answer,letter):
    for i in answer:
        if i.lower() == letter.lower():
            return True
    return False

# turtle prints "Incorrect Letters:"
def displayIncorrect():
    setPos(-125,-100)
    pen.write("Incorrect Letters:", font = style)

# adds an incorrect letter under "Incorrect Letters:"
def addIncorrect(letter,x,y):
    setPos(x,y)
    pen.write(letter, font=style2)

# displays the losing message
def losingMessage():
    turtle.reset()
    pen.reset()
    underline.clear()
    turtle.bgcolor("black")
    setPos(-50,0)
    pen.color("red")
    pen.write("GAME", font = style3)
    setPos(-50,-40)
    pen.write("OVER", font = style3)
    setPos(-125,-75)
    pen.color("white")
    pen.write(f"The correct word was: {answer}", font = style)

def drawBalloon(x,y):
    setPos(x,y)
    colors = ["red","darkorange","orange","gold","chartreuse","darkgreen","deepskyblue","blue","blueviolet","indigo","deeppink"]
    color = random.choice(colors)
    pen.setheading(90)
    pen.pensize(3)
    # balloon string
    pen.color("white")
    pen.forward(75)
    # balloon
    pen.setheading(0)
    pen.up()
    pen.backward(10)
    pen.down()
    pen.pensize(1)
    pen.color("black")
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(3):
        pen.forward(20)
        pen.left(120)
    pen.end_fill()
    pen.up()
    pen.forward(10)
    pen.left(90)
    pen.forward(13)
    pen.down()
    pen.setheading(0)
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()

def winningMessage():
    turtle.reset()
    pen.hideturtle()
    underline.hideturtle()
    pen.reset()
    pen.speed(20)
    underline.clear()
    turtle.bgcolor("black")
    for i in range(10):
        x = random.randint(-300,300)
        y = random.randint(50,200)
        drawBalloon(x,y)
    setPos(-250,0)
    pen.color("white")
    pen.write("CONGRATULATIONS, YOU WON!", font = style2)


# runs the main jeopardy code
def guessLetter(x,y):
    # global variables
    global question
    global answer
    global guessedWord
    global wrongAttemptnum
    global xCoord

    newGuessedWord = ""
    found = False
    outcome = 0
    y = -150
    incorrectLetters = []
    letter = turtle.textinput("Letter Guessing", "Enter a Letter: ")
    # checks guessed letter against letters in word
    for i in range(len(answer)):
        if answer[i].lower() == letter.lower():
            newGuessedWord += letter
            found = True
        else:
            newGuessedWord += guessedWord[i]

    # if letter isnt found
    if found == False:
        wrongAttemptnum += 1
        incorrectLetters.append(letter)
        addIncorrect(incorrectLetters[0],xCoord,y)
        incorrectLetters.clear()
        xCoord += 50

    # after 5 wrong attempts, a losing message is displayed
    if wrongAttemptnum == 5:
            pen.hideturtle()
            underline.hideturtle()
            losingMessage()

    if newGuessedWord == answer:
        winningMessage()            
        
    guessedWord = newGuessedWord
    displayWord(guessedWord)      

questionList = getQuestions()
question = random.choice(questionList)
answer = displayAnswer(question)
xCoord = -200

displayQuestion(question)
guessedWord = displayUnderscore(answer)
displayWord(guessedWord)
displayIncorrect()

wrongAttemptnum = 0

turtle.onscreenclick(guessLetter)


turtle.done()




    




