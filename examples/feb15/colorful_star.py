import turtle 
import random
turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")

colors = ("mediumorchid", "darkviolet", "darkorchid", "blueviolet", "slateblue", "mediumblue", "darkblue" )

for i in range(10):
   x =  random.randint(-turtle.window_width()//2, turtle.window_height()//2)
   y =  random.randint(-turtle.window_width()//2, turtle.window_height()//2)
   starWidth = random.randint(20,200)
   starColor = random.choice(colors)
   pen.color(starColor)
   pen.up()
   pen.setpos(x,y)
   pen.down()
   pen.begin_fill()
   for i in range(5):
       pen.forward(starWidth)
       pen.right(144)
       
   pen.end_fill()
    
    
       
           
turtle.done()