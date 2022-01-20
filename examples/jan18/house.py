import turtle # first line of evdry turtle program
turtle.bgcolor("lavender")
turtle.screensize(200,100)
pen = turtle.Turtle()

pen.color("black")
pen.pensize(5)
pen.up()
pen.setpos(-100,-100)
pen.down()

#square
pen.fillcolor("purple")
pen.begin_fill()
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.end_fill()

#setting position
pen.up()
pen.setpos(-100,100)
pen.down()

#drawing roof
pen.fillcolor("purple")
pen.begin_fill()
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.end_fill()
pen.setheading(0)

#making door
pen.up()
pen.setpos(-25,-100)
pen.down()
pen.fillcolor("brown")
pen.begin_fill()
pen.forward(50)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.end_fill()

#tree stump
pen.up()
pen.setpos(-200,-100)
pen.down()
pen.fillcolor("sienna")
pen.begin_fill()
pen.forward(30)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.end_fill()

#tree branches
pen.up()
pen.setpos(-185,40)
pen.down()
pen.fillcolor("forest green")
pen.begin_fill()
pen.circle(50)
pen.end_fill()



turtle.done() # last line of every turtle program