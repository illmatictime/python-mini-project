import turtle


#myScreen = turtle.getscreen()
def userInput():  #takes user input for number of sides and lenght of sides
    sides = int(input('Enter the number of sides of the polygon: '))
    length = int(input('Enter the length of sides: '))
    return sides, length


def angle(
    sides
):  #takes the user input of sides and calcualates angle needed for polygon
    theAngle = 180 * (sides - 2) / sides
    return theAngle


def drawShape(Turtle, sides,
              length):  # draws turtle with sides and length given
    theAngle = angle(sides)
    for x in range(sides):
        Turtle.forward(length)
        Turtle.left(180 - theAngle)


def SpinPolygon(
    Turtle, sides, angle, length, repeat
):  #creates a polygon and spins it by the by the intial angle calculated in the function angle
    for x in range(repeat):
        drawShape(Turtle, sides, length)
        Turtle.left(180 - angle)
    Turtle.left(180 - angle)


def ScalePolygon(
    Turtle, sides, length, sfactor, number
):  #scales a polygon the by sfactor with amplifies the intial size and then repeats the number of times it is drawn
    for x in range(number):
        drawShape(Turtle, sides, length)
        length = length * sfactor


def main():
    sides, length = userInput()  #user input
    theAngle = angle(sides)
    repeat = sides
    sfactor = 2
    number = 5
    t = turtle.Turtle()
    SpinPolygon(t, sides, theAngle, length, repeat)
    t.clear()
    t2 = turtle.Turtle()
    ScalePolygon(t2, sides, length, sfactor, number)
    turtle.done()  # keeps screen open
    #print(sides, length)


main()
