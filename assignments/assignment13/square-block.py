# Author: Alexandra Wheeler
# Input Block Grid
import turtle 
turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")

# Getting grid & color inputs
colors = []
numRows = int(turtle.numinput("Block", "Enter number of rows: "))
for row in range(numRows):
    color = turtle.textinput("Color", f"Enter color for row {row + 1}:").strip()
    colors.append(color)

# setting grid variables
squarewidth = turtle.window_width() // numRows
littlesquareWidth = squarewidth // 5
padding = (squarewidth - littlesquareWidth) // 2


y= -turtle.window_height()// 2 + padding



for color in colors:
    x= -turtle.window_width()// 2 + padding

    for col in range(numRows):
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.fillcolor(color)
        pen.begin_fill()
        for i in range(4):
            pen.forward(littlesquareWidth)
            pen.left(90)
        pen.end_fill()
        x+= littlesquareWidth
    y += littlesquareWidth






turtle.done()