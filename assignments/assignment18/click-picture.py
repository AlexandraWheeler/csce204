# Author: Alexandra Wheeler
# Screen Click Cars
import turtle 
import random
turtle.bgcolor("lightgray")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.speed(.5)
pen.color("black")

carWidth = 80
tireRadius = 10


def setPos(x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()

def roadMedian():
    pen.pensize(3)
    pen.color("yellow")
    setPos(-200,0)
    for i in range(10):
        pen.down()
        pen.forward(30)
        pen.up()
        pen.forward(10)
    
def drawCar(x,y):
    carBody(x,y)
    carWheels(x- tireRadius * 2,y - tireRadius* 3 ) # left tire
    carWheels(x+ tireRadius * 2,y - tireRadius* 3 ) # right tire
    pen.hideturtle()

def carBody(x,y):
    pen.color("black")
    pen.pensize(1)
    setPos(x-carWidth/2,y-carWidth/4)
    color = random.randint(1,3)
    if color == 1:
        pen.fillcolor("purple")
    if color == 2:
        pen.fillcolor("darkblue")
    if color == 3: 
        pen.fillcolor("pink")
    pen.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            pen.forward(carWidth)
            pen.left(90)
        else:
            pen.forward(carWidth/2)
            pen.left(90)
    pen.end_fill()

def carWheels(x,y):
    setPos(x,y)
    pen.fillcolor("gray")
    pen.begin_fill()
    pen.circle(tireRadius)
    pen.end_fill()

roadMedian()
turtle.onscreenclick(drawCar)


turtle.done()