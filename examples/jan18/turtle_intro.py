import turtle # first line of evdry turtle program
turtle.bgcolor("lavender")
turtle.screensize(200,100)
pen = turtle.Turtle()

pen.pensize(10)
pen.color("plum")
pen.forward(200)

#square
pen.begin_fill()
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.end_fill()

#triangle
pen.up()
pen.setpos(-200,200)
pen.down()
pen.color("blue")
pen.fillcolor("white")
pen.setheading(0)
pen.begin_fill()
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.end_fill()
pen.setheading(0)










turtle.done() # last line of every turtle program