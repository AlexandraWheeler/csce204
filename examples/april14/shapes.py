def rectangle(pen, x, y, width, length):
    setPos(pen,x,y)
    for i in range(4):
        if i % 2 == 0:
            pen.forward(length)
        else: 
            pen.forward(width)
        pen.left(90)

def square(pen,x,y,width):
    rectangle(pen,x,y,width,width)

def triangle(pen,x,y,width):
    setPos(pen,x,y)
    for i in range(3):
        pen.forward(width)
        pen.left(120)


def setPos(pen,x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()