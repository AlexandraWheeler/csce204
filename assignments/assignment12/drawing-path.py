# Author: Alexandra Wheeler
# Drawing Coordinates
import turtle 
turtle.bgcolor("lavender")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(.5)
pen.color("black")

xCoordinates = []
yCoordinates = []

# Coordinate inputs
coordinates = turtle.numinput("Coordinates", "Enter number of coordinates: ", 10, 1, 100)
for i in range(int(coordinates)):
    x = turtle.numinput("Shapes", "Enter X:", 0, -400, 400)
    xCoordinates.append(x)
    y = turtle.numinput("Shapes", "Enter Y:", 0, -400, 400)
    yCoordinates.append(y)

# Connecting the dots
pen.up
for i in range(len(xCoordinates)):
    pen.setpos(xCoordinates[i], yCoordinates[i])
    pen.down()




turtle.done()