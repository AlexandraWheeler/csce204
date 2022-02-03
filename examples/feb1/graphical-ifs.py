import turtle 
turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")

shape = turtle.textinput("Shapes", "Enter shape: ").lower().strip()

if shape == "circle":
    pen.circle(50)
elif shape == "square":
    pen.forward(50)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
elif shape == "triangle":
    pen.forward(50)
    pen.left(120)
    pen.forward(50)
    pen.left(120)
    pen.forward(50)
    pen.left(120)
else: 
    turtle.write("Not an available shape.")

turtle.done()