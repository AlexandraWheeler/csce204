import turtle 
turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")

def draw_square(x, y, width,color):
    pen.color(color)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.begin_fill()
    for i in range(4):
        pen.forward(width)
        pen.left(90)
    pen.end_fill()

draw_square(50, -100, 60, "purple")
draw_square(30, -150, 45, "pink")
draw_square(-100, 60, 75, "blue")

def draw_triangle(x, y, width,color):
    pen.color(color)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()

draw_triangle(75, 70, 45, "red")

turtle.done()
