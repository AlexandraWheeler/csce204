# Author: Alexandra Wheeler
# Drawing a ladybug


import turtle 
turtle.bgcolor("honeydew")
turtle.screensize(400,400)
pen = turtle.Turtle()

pen.speed(0)
pen.pensize(1)
pen.color("black")

# variables
drawingSize = turtle.numinput("Ladybug","Size (1, 10)", 5, 1, 10)
ladybugSize = drawingSize * turtle.window_width() / 10
ladybugHead = ladybugSize * .4
ladybugBody = ladybugSize - ladybugHead
eyeSize = ladybugHead * .15
dotSize = ladybugBody * .15

# Draw ladybug head
pen.up()
pen.setpos(-ladybugSize / 2 + ladybugHead * 1/2, -ladybugHead / 2)
pen.down
pen.fillcolor("black")
pen.begin_fill()
pen.circle(ladybugHead / 2)
pen.end_fill()

# Draw ladybug body
pen.up()
pen.setpos(ladybugSize / 2 - ladybugBody * .6 , -ladybugBody / 2)
pen.down()
pen.fillcolor("red")
pen.begin_fill()
pen.circle(ladybugBody / 2)
pen.end_fill()

# ladybug eyes
pen.up()
pen.setpos(-ladybugSize / 2 + ladybugHead * 1/3, eyeSize /2)
pen.down
pen.fillcolor("white")
pen.begin_fill()
pen.circle(eyeSize / 2)
pen.end_fill()
pen.up()
pen.setpos(-ladybugSize / 2 + ladybugHead * 1/3, -eyeSize )
pen.down
pen.fillcolor("white")
pen.begin_fill()
pen.circle(eyeSize / 2)
pen.end_fill()

# ladybug body features
# dot one
pen.up()
pen.setpos(ladybugSize / 2 - ladybugBody * .35, dotSize)
pen.down
pen.fillcolor("white")
pen.begin_fill()
pen.circle(dotSize / 2)
pen.end_fill()
pen.up()
# dot two
pen.up()
pen.setpos(ladybugSize / 2 - ladybugBody * .6, dotSize * 1/2)
pen.down
pen.fillcolor("white")
pen.begin_fill()
pen.circle(dotSize / 2)
pen.end_fill()
pen.up()
# dot three
pen.up()
pen.setpos(ladybugSize / 2 - ladybugBody * .85, dotSize)
pen.down
pen.fillcolor("white")
pen.begin_fill()
pen.circle(dotSize / 2)
pen.end_fill()
pen.up()
# dot four
pen.up()
pen.setpos(ladybugSize / 2 - ladybugBody * .35, -dotSize * 2)
pen.down
pen.fillcolor("white")
pen.begin_fill()
pen.circle(dotSize / 2)
pen.end_fill()
pen.up()
# dot five
pen.up()
pen.setpos(ladybugSize / 2 - ladybugBody * .6, -dotSize * 3/2)
pen.down
pen.fillcolor("white")
pen.begin_fill()
pen.circle(dotSize / 2)
pen.end_fill()
pen.up()
# dot six
pen.up()
pen.setpos(ladybugSize / 2 - ladybugBody * .85, -dotSize * 2)
pen.down
pen.fillcolor("white")
pen.begin_fill()
pen.circle(dotSize / 2)
pen.end_fill()
pen.up()
#line
pen.up()
pen.setpos(-ladybugBody * .275 , 0)
pen.down()
pen.pensize(10)
pen.pencolor("black")
pen.forward(ladybugBody)

turtle.done()