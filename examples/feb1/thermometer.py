import turtle 
turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")
style = ("Arial", 12, "normal")

# draw thermometer
tHeight = 200
tWidth = tHeight / 4
pen.up()
pen.setpos(-tWidth/2,-tHeight/2)
pen.down()
pen.forward(tWidth)
pen.left(90)
pen.forward(tHeight)
pen.left(90)
pen.up()
pen.forward(tWidth)
pen.left(90)
pen.down()
pen.forward(tHeight)

# thermometer markings
# 0%
turtle.up()
turtle.setpos(tWidth/2 + 10, -tHeight/2)
turtle.down()
turtle.write("0%",  font = style)

# 25%
turtle.up()
turtle.setpos(tWidth/2 + 10, -tHeight/4)
turtle.down()
turtle.write("25%",  font = style)

# 50%
turtle.up()
turtle.setpos(tWidth/2 + 10, 0)
turtle.down()
turtle.write("50%",  font = style)

# 75%
turtle.up()
turtle.setpos(tWidth/2 + 10, tHeight/4)
turtle.down()
turtle.write("75%",  font = style)

# 100%
turtle.up()
turtle.setpos(tWidth/2 + 10, tHeight/2)
turtle.down()
turtle.write("100%",  font = style)

# get donations
donations = turtle.numinput("Donations", "Enter total donations:")
goal = 10000
percentGoal = donations/goal
 
# error case donations
if percentGoal < 0:
    percentGoal = 0
elif percentGoal > 1:
    percentGoal = 1

dHeight = tHeight * percentGoal

# draw current donations
pen.up()
pen.setpos(-tWidth/2,-tHeight/2)
pen.down()
pen.fillcolor("red")
pen.begin_fill()
pen.setheading(0)

pen.forward(tWidth)
pen.left(90)
pen.forward(dHeight)
pen.left(90)
pen.forward(tWidth)
pen.left(90)
pen.forward(dHeight)
pen.left(90)
pen.end_fill()

# reached goal
if percentGoal >= 1:
    turtle.up()
    turtle.setpos(-tWidth/2,tHeight/2 + 20)
    turtle.down()
    turtle.write("Goal achieved!", font = style)







turtle.done()