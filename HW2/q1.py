# Question Number One

import turtle
import math

draw = turtle.Turtle()
draw.screen.bgcolor("#99d6ff")
draw.pensize(2)
draw.hideturtle()
number = draw.screen.numinput(
    "draw a shape", "From 1 to 6 enter a number. (number 0 to exit)", minval=0, maxval=6)


def shape_one():

    draw.color("black", "white")

    draw.begin_fill()

    draw.right(45)

    for _ in range(3):
        draw.forward(100)
        draw.left(90)

    draw.forward(100)

    for _ in range(3):
        draw.forward(100)
        draw.right(90)

    draw.forward(100)

    draw.end_fill()


def shape_two():

    draw.color("black", "white")

    for _ in range(3):
        draw.forward(300)
        draw.left(120)

    draw.begin_fill()

    draw.left(45)
    draw.forward(210)
    draw.right(90)
    draw.forward(210)

    draw.end_fill()


def shape_three():
    WIDTH = 200
    HEIGHT = (math.sqrt(WIDTH ** 2 + WIDTH ** 2))

    for _ in range(4):
        draw.forward(WIDTH)
        draw.left(90)

    draw.forward(WIDTH)

    for _ in range(4):
        draw.forward(WIDTH)
        draw.right(90)

    draw.right(45)
    draw.forward(HEIGHT)
    draw.backward(2 * HEIGHT)

    draw.left(45)
    draw.forward(WIDTH)
    draw.right(45)
    draw.forward(HEIGHT)

    draw.backward(HEIGHT)
    draw.left(45)
    draw.backward(WIDTH)
    draw.right(90)
    draw.forward(WIDTH)

    draw.left(45)
    draw.forward(HEIGHT)


def shape_four():
    RADIUS = 50

    draw.penup()
    draw.goto(-200, 200)
    draw.pendown()

    for _ in range(2):
        draw.circle(RADIUS)

        draw.forward(15)

        draw.right(90)
        draw.circle(RADIUS)
        draw.circle(RADIUS, 180)

        draw.forward(4)

        draw.right(90)
        draw.circle(RADIUS)


def shape_five():

    draw.circle(50)

    draw.penup()
    draw.left(90)
    draw.forward(50)
    draw.right(90)
    draw.pendown()

    for _ in range(4):
        draw.forward(200)
        draw.backward(200)
        draw.left(90)

    draw.penup()

    draw.right(2)
    draw.forward(240)
    draw.write("East", align="right", font=("Arial", 12))
    draw.backward(240)
    draw.left(2)

    draw.left(180)

    draw.left(2)
    draw.forward(240)
    draw.write("West", align="left", font=("Arial", 12))
    draw.backward(240)
    draw.right(2)

    draw.right(90)
    draw.forward(200)
    draw.write("North", align="center", font=("Arial", 12))

    draw.right(180)
    draw.forward(200 * 2)
    draw.penup()
    draw.forward(20)
    draw.write("South", align="center", font=("Arial", 12))


def shape_six():
    HEIGHT = 200
    DIAGONAL = math.sqrt(200 ** 2 + 200 ** 2)

    draw.dot(10)
    draw.left(45)

    draw.forward(DIAGONAL / 2)
    draw.dot(10)
    draw.forward(DIAGONAL / 2)
    draw.dot(10)
    draw.right(135)
    draw.forward(HEIGHT)
    draw.dot(10)
    draw.right(135)

    draw.forward(DIAGONAL / 2)
    draw.forward(DIAGONAL / 2)
    draw.dot(10)
    draw.left(135)
    draw.forward(HEIGHT)
    draw.dot(10)

    draw.left(90)
    draw_dash()

    draw.left(135)
    draw.forward(DIAGONAL)
    draw.right(135)
    draw_dash()


def draw_dash():
    i = 2
    for _ in range(8):
        if i % 2 == 0:
            draw.forward(35)
        else:
            draw.penup()
            draw.forward(15)
            draw.pendown()
        i += 1


match number:
    case 0:
        exit(0)
    case 1:
        shape_one()
    case 2:
        shape_two()
    case 3:
        shape_three()
    case 4:
        shape_four()
    case 5:
        shape_five()
    case 6:
        shape_six()

draw.screen.mainloop()
