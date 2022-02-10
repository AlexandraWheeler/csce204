import turtle 
turtle.bgcolor("lavender")
turtle.setup(400,400)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")

trunkWidth = turtle.window_width() // 10
treeLg = trunkWidth * 3
mdTree = treeLg * 2/3
smTree = mdTree * 2/3
starWidth = smTree * 1/2
pen.up()
pen.setpos(-trunkWidth //2, -treeLg * 3/2)

# draw trunk
pen.color("sienna")
pen.begin_fill()
for i in range(4):
    pen.forward(trunkWidth)
    pen.left(90)
pen.end_fill()

# draw tree
pen.color("green")
pen.up()
pen.setpos(-treeLg // 2, -treeLg * 3/2 + trunkWidth)
pen.down()
pen.begin_fill()
for i in range(3):
    pen.forward(treeLg)
    pen.left(120)
pen.end_fill()

pen.color("green")
pen.up()
pen.setpos(-mdTree // 2, -treeLg * 3/2 + trunkWidth + treeLg * 1/2)
pen.down()
pen.begin_fill()
for i in range(3):
    pen.forward(mdTree)
    pen.left(120)
pen.end_fill()

pen.color("green")
pen.up()
pen.setpos(-smTree // 2, -treeLg * 3/2 + trunkWidth + treeLg * 1/2 + mdTree // 2)
pen.down()
pen.begin_fill()
for i in range(3):
    pen.forward(smTree)
    pen.left(120)
pen.end_fill()

pen.color("gold")
pen.up()
pen.setpos(-starWidth //2, -treeLg * 3/2 + trunkWidth + treeLg * 1/2 + mdTree //2 + smTree * 3/4)
pen.down()
pen.begin_fill()
for i in range(3):
    pen.forward(starWidth)
    pen.left(120)
pen.end_fill()
pen.color("gold")
pen.up()
pen.setpos(-starWidth //2, -treeLg * 3/2 + trunkWidth + treeLg * 1/2 + mdTree //2 + smTree)
pen.down()
pen.begin_fill()
for i in range(3):
    pen.forward(starWidth)
    pen.left(-120)
pen.end_fill()


turtle.done()