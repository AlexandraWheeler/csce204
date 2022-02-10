from tkinter import font
import turtle 
import random
turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")
style = ("Verdana", 12, "normal")
turtle.colormode(255)


userName = turtle.textinput("Names", "Enter name: ")
numNames = int(turtle.numinput("Names", "Enter number of names: ", 10, 1, 100))

for i in range(numNames):
    x = random.randint(-turtle.window_width() // 2, turtle.window_width() //2 )
    y = random.randint(-turtle.window_height() // 2, turtle.window_height() //2 )
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    pen.color(r,g,b)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.write(userName, font = style)

turtle.done()