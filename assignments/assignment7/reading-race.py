#Author: Alexandra Wheeler
# Graphical ifs: Reading Log 

import turtle 
turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")
style = ("Arial", 40, "normal")

circleSize = 100
pen.up()
pen.setpos(0,-circleSize)
pen.down()

numBooks = turtle.numinput("Reading Log", "How many books have you read this month: ")

if numBooks >= 30:
    # making circles
    pen.color("dark goldenrod")
    pen.fillcolor("dark goldenrod")
    pen.begin_fill()
    pen.circle(circleSize)
    pen.end_fill()
    pen.up()
    pen.setpos(0,-circleSize + 10)
    pen.down()
    pen.color("wheat")
    pen.fillcolor("wheat")
    pen.begin_fill()
    pen.circle(circleSize - 10)
    pen.end_fill()
    pen.up()
    # writing $10
    turtle.up()
    turtle.setpos(-32,-22)
    turtle.down()
    turtle.color("dark goldenrod")
    turtle.write("$10", font = style)
    turtle.up()
elif numBooks >= 15:
    # making circles
    pen.color("dark gray")
    pen.fillcolor("dark gray")
    pen.begin_fill()
    pen.circle(circleSize)
    pen.end_fill()
    pen.up()
    pen.setpos(0,-circleSize + 10)
    pen.down()
    pen.color("gainsboro")
    pen.fillcolor("gainsboro")
    pen.begin_fill()
    pen.circle(circleSize - 10)
    pen.end_fill()
    pen.up()
    # writing $5
    turtle.up()
    turtle.setpos(-20,-22)
    turtle.down()
    turtle.color("dark gray")
    turtle.write("$5", font = style)
    turtle.up()
elif numBooks >= 5:
    # making circles
    pen.color("saddle brown")
    pen.fillcolor("saddle brown")
    pen.begin_fill()
    pen.circle(circleSize)
    pen.end_fill()
    pen.up()
    pen.setpos(0,-circleSize + 10)
    pen.down()
    pen.color("burlywood")
    pen.fillcolor("burlywood")
    pen.begin_fill()
    pen.circle(circleSize - 10)
    pen.end_fill()
    pen.up()
    # writing $2
    turtle.up()
    turtle.setpos(-20,-22)
    turtle.down()
    turtle.color("saddle brown")
    turtle.write("$2", font = style)
    turtle.up()
elif numBooks >= 0:
    # making circles
    pen.color("red")
    pen.fillcolor("red")
    pen.begin_fill()
    pen.circle(circleSize)
    pen.end_fill()
    pen.up()
    pen.setpos(0,-circleSize + 10)
    pen.down()
    pen.color("white")
    pen.fillcolor("white")
    pen.begin_fill()
    pen.circle(circleSize - 10)
    pen.end_fill()
    pen.up()
    # writing $0
    turtle.up()
    turtle.setpos(-20,-22)
    turtle.down()
    turtle.color("red")
    turtle.write("$0", font = style)
    turtle.up()


turtle.done()