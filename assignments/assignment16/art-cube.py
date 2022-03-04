#Author: Alexandra Wheeler
# Drawing art cube
import turtle 
import random
turtle.bgcolor("lavender")
turtle.colormode(255)
turtle.screensize(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)




pen.forward(5)

def draw_triangle(width):
    pen.up()
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = [r,g,b]   
    pen.fillcolor(rgb)
    pen.begin_fill()
    pen.down()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()


def draw_cube(x,y,width):
    pen.up()
    pen.setpos(x,y)
    pen.down
    for i in range(6):
        draw_triangle(width/2)
        pen.left(60)

for i in range(20):
    x= random.randint(-200,200)
    y= random.randint(-200,200)
    width = random.randint(10,100)
    draw_cube(x,y,width)

turtle.done()
