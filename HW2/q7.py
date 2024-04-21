import turtle

snow = turtle.Turtle()
snow.penup()
snow.goto(0, -375)
snow.pendown()
snow.pensize(2)
snow.speed(100)
snow.hideturtle()
snow.screen.bgcolor("#99d6ff")

BASE_RADIUS = 200
MID_RADIUS = 100


def drawBase():
    snow.circle(BASE_RADIUS)


def drawMidSection():
    snow.circle(MID_RADIUS)


def drawArms():
    snow.left(45)
    snow.forward(70)

    snow.right(25)
    snow.forward(25)

    snow.backward(25)

    snow.left(90)
    snow.forward(25)

    snow.backward(25)

    snow.left(115)
    snow.forward(70)

    snow.right(45)

    snow.penup()
    snow.forward(200)
    snow.pendown()

    snow.right(25)
    snow.forward(50)
    snow.right(40)
    snow.forward(50)

    snow.right(30)
    snow.forward(20)
    snow.backward(20)
    snow.left(60)
    snow.forward(30)


def drawHead():
    snow.color("black", "white")
    snow.circle(50)

    snow.penup()
    snow.left(90)
    snow.forward(40)
    snow.right(90)
    snow.backward(20)
    snow.pendown()

    snow.forward(50)

    snow.penup()
    snow.left(90)
    snow.forward(30)
    snow.pendown()
    snow.begin_fill()
    snow.circle(5)

    snow.penup()
    snow.left(90)
    snow.forward(50)
    snow.pendown()

    snow.circle(5)
    snow.end_fill()


def drawHat():
    snow.color("black", "black")

    snow.begin_fill()
    for _ in range(2):
        snow.forward(100)
        snow.left(90)
        snow.forward(20)
        snow.left(90)
    snow.end_fill()

    snow.left(90)
    snow.forward(20)
    snow.right(90)
    snow.forward(80)

    snow.begin_fill()
    for _ in range(4):
        snow.left(90)
        snow.forward(60)
    snow.end_fill()


drawBase()

snow.penup()
snow.left(90)
snow.forward(2 * BASE_RADIUS)
snow.right(90)
snow.pendown()

drawMidSection()

snow.penup()

snow.left(90)
snow.forward(2 * MID_RADIUS)
snow.right(90)

snow.pendown()

drawHead()

snow.penup()
snow.forward(30)
snow.right(90)
snow.forward(20)
snow.right(90)
snow.pendown()

drawHat()

snow.penup()
snow.forward(70)
snow.right(90)
snow.forward(2 * MID_RADIUS)
snow.left(90)
snow.pendown()

drawArms()


snow.screen.mainloop()
