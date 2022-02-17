import turtle 
turtle.bgcolor("skyblue")
turtle.setup(600,600)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")

gridsize = int(turtle.numinput("Size", "Enter Size:", 5, 1, 10))
treesqaureW = turtle.window_width() // gridsize

trunkWidth = treesqaureW // 5
padding = (treesqaureW - trunkWidth) // 2
treetrunkH = trunkWidth * 3
leafRadius = trunkWidth * 1.25
x = -turtle.window_width() // 2 + padding
y = -turtle.window_height() // 2 + padding

for row in range( gridsize):
    x = -turtle.window_width() // 2 + padding
    for col in range(gridsize):
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.color("brown")
        pen.begin_fill()
        for i in range(4):
            if i % 2 == 0:
                pen.forward(trunkWidth)
            else:
                pen.forward(treetrunkH)
            pen.left(90)
        pen.end_fill()

        pen.up()
        pen.setpos(x + trunkWidth // 2, y + treetrunkH * .8)

        pen.color("green")
        pen.begin_fill()
        pen.circle(leafRadius)
        pen.end_fill()
        

       
        x += treesqaureW 
    y += treesqaureW



turtle.done()