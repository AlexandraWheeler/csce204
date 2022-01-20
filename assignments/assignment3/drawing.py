# Drawing of a cat
# Author: Alexandra Wheeler 01/19/2021
import turtle 
turtle.bgcolor("lavender")
turtle.screensize(200,100)
pen = turtle.Turtle()

pen.color("orange")
pen.pensize(1)
pen.up()
pen.setpos(-75,-50)
pen.down()
# Making body of cat
pen.fillcolor("orange")
pen.begin_fill()
pen.forward(150)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.end_fill()

pen.fillcolor("orange")
pen.begin_fill()
pen.circle(50)
pen.end_fill()
pen.up()
pen.setpos(75,-50)
pen.down()
pen.fillcolor("orange")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# Making cat head
pen.up()
pen.setpos(120,30)
pen.down()
pen.fillcolor("orange")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# Making face features
pen.up()
pen.setpos(100,120)
pen.down()
# cat ear one
pen.fillcolor("orange")
pen.begin_fill()
pen.left(10)
pen.forward(30)
pen.left(120)
pen.forward(30)
pen.left(120)
pen.forward(30)
pen.left(120)
pen.end_fill()

# cat ear two
pen.up()
pen.setpos(170,90)
pen.down()
pen.fillcolor("orange")
pen.begin_fill()
pen.left(50)
pen.forward(30)
pen.left(120)
pen.forward(30)
pen.left(120)
pen.forward(30)
pen.left(120)
pen.end_fill()

# cat eyes
pen.up()
pen.setpos(120,100)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(5)
pen.end_fill()
pen.up()
pen.setpos(145,85)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(5)
pen.end_fill()

# cat nose
pen.up()
pen.setpos(123,75)
pen.down()
pen.fillcolor("pink")
pen.begin_fill()
pen.circle(5)
pen.end_fill()

# cat leg one
pen.up()
pen.setpos(110,0)
pen.down()
pen.fillcolor("orange")
pen.begin_fill()
pen.left(300)
pen.left(270)
pen.forward(125)
pen.left(270)
pen.forward(30)
pen.left(270)
pen.forward(125)
pen.left(270)
pen.forward(30)
pen.end_fill()

# cat leg two
pen.up()
pen.setpos(-110,0)
pen.down()
pen.fillcolor("orange")
pen.begin_fill()
pen.left(270)
pen.forward(125)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(125)
pen.left(90)
pen.forward(30)
pen.end_fill()

# cat tail
pen.up()
pen.setpos(-90,20)
pen.down()
pen.fillcolor("orange")
pen.begin_fill()
pen.left(315)
pen.forward(125)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(125)
pen.left(90)
pen.forward(30)
pen.end_fill()








turtle.done() 