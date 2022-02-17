import turtle 
turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(10)
pen.speed(.5)
pen.color("black")

colors = ("violet", "indigo", "blue", "green", "yellow", "orange", "red")
radius = turtle.window_width()//6
y = 0

for color in colors:
    pen.up()
    pen.setpos(0,y)
    pen.down()
    
    pen.color(color)
    pen.setheading(90)
    pen.circle(radius, 180)
    y+=10


turtle.done()