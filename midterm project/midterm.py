# Author: Alexandra Wheeler
# Beautiful Stars
import turtle
import random 
turtle.bgcolor("black")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(1)
pen.color("black")
style = ("Arial", 15, "normal")
styleHeading = ("Arial", 24, "normal")

# user input
starColors = []
starNames = []
stars = int(turtle.numinput("Stars", "How many stars?", 5, 1, 10))
for num in range(stars):
    color = turtle.textinput("Color", f"Enter color for star {num + 1}:").strip()
    starColors.append(color)
    name = turtle.textinput("Name", f"Enter name for star {num + 1}:").strip()
    starNames.append(name)

# variables for stars
starboxWidth = turtle.window_width() // stars
starWidth = starboxWidth // 4
padding = (starboxWidth-starWidth) // 2



# writing "beautiful stars"
turtle.up()
turtle.setpos(-turtle.window_width()//2 + 50, turtle.window_height()//2 - 50)
turtle.down()
turtle.color("White")
turtle.write("Beautiful Stars", font = styleHeading)
s = 0
x = -turtle.window_width() // 2 + padding
# drawing stars
for color in starColors:
    y = random.randint(-turtle.window_height() // 2 + 10, turtle.window_height() //2 - 100)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    if color == "blue":
      # draw cloud
        for i in range(3):
            pen.begin_fill()
            pen.circle(starWidth // 2)
            pen.forward(starWidth // 2)
            pen.end_fill()
    elif color == "yellow":
        # draw sun
        pen.begin_fill()
        pen.circle(starWidth * .6)
        pen.end_fill()
    else:
        # draw star
        for i in range(2):
            pen.begin_fill()
            for i in range(3):
                pen.forward(starWidth)
                pen.left(120)
            pen.end_fill()
            pen.up
            pen.setpos(x+starWidth, y+ starWidth // 2)
            pen.down
            pen.left(180)
    pen.up()
    pen.setpos(x,y + starWidth)
    pen.color("white")
    pen.write(starNames[s], font=style)
    x+=starboxWidth
    s+=1


turtle.done()