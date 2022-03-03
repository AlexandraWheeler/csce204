import turtle 
turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")

def draw_square(x, y, width,color):
    draw_rectangle(x,y,width,width,color)

def draw_circle(x,y,radius,color):
    pen.color(color)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_rectangle(x,y,width,length,color):
    pen.color(color)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            pen.forward(width)
        else:
            pen.forward(length)
        pen.left(90)
    pen.end_fill()

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

# draw house
draw_square(-50,-50, 100, "brown")
draw_triangle(-60,35,120,"black")
draw_rectangle(-15, -50, 30, 60, "red")
draw_circle(10,-25,5,"black")





turtle.done()