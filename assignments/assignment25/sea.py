import random
from boat import Boat
import turtle 
turtle.bgcolor("skyblue")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")

def randomColor():
    colorList = ['firebrick', 'darkred', 'coral', 'darkorange', 'gold', 'lemonchiffon', 'yellowgreen', 'lightseagreen', 'deepskyblue', 'mediumblue', 'navy', 'blueviolet', 'indigo', 'orchid']
    color = random.choice(colorList)
    return color

def randomX():
    xCoord = random.randint(-400,400)
    return int(xCoord)

def randomY():
    yCoord = random.randint(-400,400)
    return int(yCoord)

def randHeight():
    height = random.randint(10,100)
    return int(height)


boats = []
for i in range(10):
    myBoat = Boat(randomX(),randomY(),randHeight(),randomColor())
    boats.append(myBoat)
    
for boat in boats:
    boat.draw(pen)



turtle.done()

