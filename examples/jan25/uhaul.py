import turtle # first line of evdry turtle program
turtle.bgcolor("skyblue")
turtle.screensize(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.color("red")
pen.speed(0)

drawingSize = turtle.numinput("Uhaul","Size (1, 5)", 3, 1, 5)
uhaulSize= drawingSize * turtle.window_width() / 5
truckWidth = uhaulSize * 3/4
cabWidth = uhaulSize - truckWidth
truckHeight = uhaulSize * 3/4
capHeight = truckHeight * 1/2
wheelWidth = uhaulSize * .1


# truck body
pen.up()
pen.setpos(-uhaulSize * 1/2, -truckHeight * 1/2)
pen.down()
pen.begin_fill()
pen.forward(uhaulSize)
pen.left(90)
pen.forward(capHeight)
pen.left(90)
pen.forward(cabWidth)
pen.left(270)
pen.forward(truckHeight-capHeight)
pen.left(90)
pen.forward(truckWidth)
pen.left(90)
pen.forward(truckHeight)
pen.left(90)
pen.end_fill()

# truck wheels
pen.up()
pen.setpos(-uhaulSize + uhaulSize * .75, -truckHeight * 1/2 - wheelWidth * 3/4)
pen.down
pen.fillcolor("Black")
pen.begin_fill()
pen.circle(wheelWidth)
pen.end_fill()




turtle.done()