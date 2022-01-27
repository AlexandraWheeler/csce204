# Create a snowman
# Author: Portia Plante
import turtle # first line of evdry turtle program
turtle.bgcolor("skyblue")
turtle.screensize(400,400)
pen = turtle.Turtle()

pen.speed(0)
pen.pensize(1)
pen.color("black")
pen.fillcolor("white")

# title, prompt, default, min, max
drawingSize = turtle.numinput("Snowman","Size (1, 5)", 3, 1, 5)

#snowmanSize = turtle.numinput("Snowman", "Enter a number between 50-800 ")
snowmanSize= drawingSize * turtle.window_height() / 5
largeCircle = snowmanSize // 3
mediumCircle = largeCircle * 3/4
smallCircle= mediumCircle * 3/4

# Draw large circle
pen.up()
pen.setpos(0,-snowmanSize/2)
pen.down()
pen.begin_fill()
pen.circle(largeCircle / 2)
pen.end_fill()

# Draw medium circle
pen.up()
pen.setpos(0,-snowmanSize / 2 +largeCircle * 3/4)
pen.down()
pen.begin_fill()
pen.circle(mediumCircle / 2)
pen.end_fill()

# Draw small circle
pen.up()
pen.setpos(0,-snowmanSize / 2 +largeCircle * 3/4 + mediumCircle * 3/4)
pen.down()
pen.begin_fill()
pen.circle(smallCircle / 2)
pen.end_fill()


turtle.done()