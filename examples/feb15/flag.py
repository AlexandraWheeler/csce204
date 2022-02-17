import turtle 
turtle.bgcolor("white")
turtle.setup(600,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")

x = -turtle.window_width() // 2
y = -turtle.window_height() // 2
stripeWidth = turtle.window_width()
stripeHeight =  turtle.window_height()/13

# draw red stripes
for i in range(7):
    pen.up()
    pen.setpos(x,y)
    pen.down()
     # draw stripe
    y += stripeHeight * 2
    pen.color("red")
    pen.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            pen.forward(stripeWidth)
        else:
            pen.forward(stripeHeight)
        pen.left(90)
    pen.end_fill()
    #for i in range(2):
        #pen.color("red")
        #pen.begin_fill()
        #pen.forward(stripeWidth)
        #pen.left(90)
        #pen.forward(stripeHeight)
        #pen.left(90)
        #pen.end_fill()
    pen.setheading(0)

# draw blue square
squareW =  turtle.window_width() / 2.25
squareH = turtle.window_height() * 7/13
x = -turtle.window_width()//2
y = -turtle.window_height()//2 + (turtle.window_height() - squareH)
pen.up()
pen.setpos(x,y)
pen.down()
pen.color("blue")
pen.begin_fill()
for i in range(4):
        if i % 2 == 0:
            pen.forward(squareW)
        else:
            pen.forward(squareH)
        pen.left(90)
pen.end_fill()

# stars
starboxW = squareW / 6
starboxH = squareH / 9
star6padding = starboxW / 4
star9padding = starboxW / 2
starWidth = 5

x = -turtle.window_width()//2 + starboxW // 2
y = -turtle.window_height()//2 + (turtle.window_height() - squareH) + starboxH
pen.up()
pen.setpos(x,y)
pen.down()
angle = 120

for row in range(10):
    x = -turtle.window_width()//2 + starboxW // 3
    for i in range(5):
        x += star6padding
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.color("white")
        pen.begin_fill()
        pen.left(10)
        for side in range(5):
            pen.forward(starWidth)
            pen.right(angle)
            pen.forward(starWidth)
            pen.right(72 - angle)
        pen.end_fill()
        x += starboxW // 1.5 + star6padding
        pen.setheading(0)
    y += star9padding  



turtle.done()