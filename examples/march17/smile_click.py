import turtle 
import random
turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")

faceRadius = 30

def drawFace(x,y):
    drawHead(x,y)
    drawEye(x-faceRadius*.4,y+faceRadius/10)
    drawEye(x+faceRadius*.4,y+faceRadius/10)
    drawMouth(x,y-faceRadius*.5)
    pen.hideturtle()

def drawHead(x,y):
    setPos(x,y - faceRadius)
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.circle(faceRadius)
    pen.end_fill()


def drawEye(x,y):
    eyeRadius = faceRadius / 5
    setPos(x,y - eyeRadius)
    pen.fillcolor("black")
    if random.randint(0,1) == 0:
        pen.begin_fill()
        pen.circle(eyeRadius)
        pen.end_fill()
    else:
        setPos(x-eyeRadius,y)
        pen.forward(eyeRadius)
    



def drawMouth(x,y):
    mouthRadius = faceRadius * .5
    setPos(x-mouthRadius*.85,y)
    pen.fillcolor("black")
    if random.randint(0,1) == 0:
        pen.left(-60)
        pen.circle(mouthRadius,120)
    else:
        setPos(x,y-mouthRadius/2)
        pen.fillcolor("pink")
        pen.begin_fill()
        pen.circle(mouthRadius/2)
        pen.end_fill()

   

def setPos(x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()


turtle.onscreenclick(drawFace)


turtle.done()