import turtle 
turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")

# drawing square
pen.up()
pen.setpos(50,50)
pen.down()
length = 50

pen.fillcolor("magenta")
pen.begin_fill()
for i in range(4):
    pen.forward(length)
    pen.left(90)
pen.end_fill()

pen.up()
pen.setpos(-50,-50)
pen.down()
pen.fillcolor("blue")
pen.begin_fill()
for i in range(3):
    pen.forward(length)
    pen.left(120)
pen.end_fill()

pen.up()
pen.setpos(-50,-60)
pen.down()
pen.fillcolor("blue")
pen.begin_fill()
for i in range(3):
    pen.forward(length)
    pen.left(-120)
pen.end_fill()


turtle.done()