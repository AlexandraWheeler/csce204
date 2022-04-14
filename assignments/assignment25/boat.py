from turtle import color
import random


class Boat:
    def __init__(self,x,y,height,color):
        self.x = x
        self.y = y
        self.height = height
        self.color = color

    def draw(self, pen):
        pen.setheading(0)
        self.setPos(pen,self.x - self.height//2, self.y - self.height//2)
        self.drawBoat(pen)
        self.drawPole(pen)
        self.drawFlag(pen)
        
    def drawBoat(self,pen):
        pen.fillcolor(self.color)
        pen.begin_fill()
        for i in range(4):
            i += 1
            if i % 2 == 0:
                pen.forward(self.height * .5)
                pen.left(120)
            elif i % 3 == 0:
                pen.forward(self.height * 1.2)
                pen.left(120)
            else:
                pen.forward(self.height * .7)
                pen.left(60)
        pen.end_fill()

    def drawPole(self,pen):
        self.setPos(pen,self.x - self.height * .1, self.y - self.height//6)
        pen.pensize(2)
        pen.left(30)
        pen.forward(self.height * .8)
    
    def drawFlag(self,pen):
        pen.fillcolor(self.color)
        pen.pensize(1)
        pen.begin_fill()
        for i in range(3):
            pen.left(120)
            pen.forward(self.height * .3)
        pen.end_fill()

    

                



    def setPos(self, pen, x, y):
        pen.up()
        pen.setpos(x,y)
        pen.down()


