import turtle

# myScreen = turtle.getscreen()


def movePen(theTurtle):
    theTurtle.penup()  # picks up pen, move without drawing
    theTurtle.forward(10)
    theTurtle.right(90)
    theTurtle.forward(10)
    theTurtle.left(90)
    theTurtle.pendown()  # puts pen down, to resume drawing


def createSquare(theTurtle, length):
    for x in range(4):
        theTurtle.forward(length)  # creates the square
        theTurtle.right(90)


def main():
    theTurtle = turtle.Turtle()
    length = 120
    while length > 0:
        createSquare(theTurtle, length)
        movePen(theTurtle)

        length = length - 20  # reduces the length to shrink size of square

    turtle.done()  # keeps screen open


main()
