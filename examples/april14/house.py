import turtle
import shapes as sh

turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")

sh.square(pen,-50,-50,100)
sh.triangle(pen,-70,50,140)
sh.rectangle(pen,-15,-50,50,30)


turtle.done()