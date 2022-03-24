# Author: Alexandra Wheeler
# Drawing Trees and Flowers from txt File

import turtle 

turtle.bgcolor("palegreen")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")
pen.hideturtle()

def getScene():
    scene = []
    try: 
        with open("assignments/assignment20/scene.txt") as file:
            for line in file:
                scene.append(line.strip().lower())
    except FileNotFoundError:
        print("File does not exist")
    return scene

def setPos(x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()

def drawFlower(x,y,size):
    pen.pensize(3)
    setPos(x,y)
    radius = size * .1
    pen.left(90)
    pen.color("darkolivegreen")
    pen.forward(size * .9)
    pen.color("violet")
    for i in range(5):
        pen.circle(radius)
        pen.left(72)

def drawTree(x,y,size):
    pen.pensize(10)
    setPos(x,y+1)
    radius = size * .2
    pen.left(90)
    pen.color("saddlebrown")
    pen.forward(size)
    pen.color("forestgreen")
    pen.begin_fill()
    pen.left(90)
    pen.circle(radius)
    pen.end_fill()

myScene = getScene()
squareWidth = int(turtle.window_width())/ (len(myScene)*2)
size = int(turtle.window_height())/5
y = -size // 2
x = -turtle.window_width()/2  + squareWidth

# drawing scene
for plant in myScene:
    if plant == "tree":
        drawTree(x,y,size)
    if plant == "flower":
        drawFlower(x,y,size)
    x+=squareWidth * 2
    pen.setheading(0)
        




turtle.done()