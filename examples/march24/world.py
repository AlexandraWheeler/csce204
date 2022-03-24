import turtle 
import random
turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")
pen.hideturtle()

def getColors():
    colors = []
    try:
        with open("examples/march24/colors.txt") as file:
            for line in file:
                colors.append(line.strip())
    except FileNotFoundError:
        print("Your color file does not exist.")

    return colors

def drawColors(y,height,color):
    x = -(int(turtle.window_width()/2))
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            pen.forward(int(turtle.window_width()))
            pen.left(90)
        else:
            pen.forward(height)
            pen.left(90)
    pen.end_fill()


myColors = getColors()
y = -turtle.window_width()/2
height = int(turtle.window_width()) / len(myColors)

for color in myColors:
    drawColors(y,height,color)
    y += height



turtle.done()