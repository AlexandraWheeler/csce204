import turtle 
turtle.bgcolor("black")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(0)
pen.color("magenta")

hexLength = turtle.window_width() // 9
x = -hexLength * 2.5
y = hexLength * 2.5
pen.up()
pen.setpos(x,y)
pen.down()
for i in range(5):
    pen.fillcolor("aqua")
    pen.begin_fill()
    for i in range(6):
        pen.left(60)
        pen.forward(hexLength)
    pen.end_fill()
    pen.up()
    x += hexLength * 1.5 + 5
    y -= hexLength 
    pen.setpos(x,y)
    pen.down()





turtle.done()