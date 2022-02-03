import turtle 
turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")

pen.up()
pen.setpos(-turtle.window_width()/2,0)
pen.down()
pen.forward(turtle.window_width())
pen.up()
pen.setpos(0,-turtle.window_height()/2)
pen.setheading(90)
pen.down()
pen.forward(turtle.window_height())

arcRadius = 50

# Smile
#pen.up()
#pen.setpos(-arcRadius,0)
#pen.down()
#pen.setheading(-60)
#pen.circle(arcRadius, 120)

# frown
pen.up()
pen.setpos(arcRadius,-arcRadius)
pen.down()
pen.setheading(120)
pen.circle(arcRadius, 120)



turtle.done()