# Question number 10

import turtle
import random

build = turtle.Turtle()
build.hideturtle()
build.penup()
build.screen.setworldcoordinates(-300, -300, 150, 150)
build.goto(-300, -300)
build.pendown()

build.speed(10)


def drawOutline():

    build.color("black", "gray")

    build.begin_fill()

    build.left(90)
    build.forward(125)

    # 1
    build.right(90)
    build.forward(60)

    # 2
    build.left(90)
    build.forward(80)

    # 3
    build.right(90)
    build.forward(60)

    # 4
    build.left(90)
    build.forward(180)

    # 5
    build.right(90)
    build.forward(120)

    # 6
    build.right(90)
    build.forward(220)

    # 7
    build.left(90)
    build.forward(60)

    # 8
    build.left(90)
    build.forward(110)

    # 9
    build.right(90)
    build.forward(70)

    # 10
    build.right(90)
    build.forward((3/4) * 110)

    # 11
    build.left(90)
    build.forward(30)

    # 12
    build.right(90)
    build.forward(80)

    # 13
    build.left(90)
    build.forward(50)

    build.right(90)
    build.forward(112)

    build.end_fill()


def windows():
    build.color("white", "white")

    build.begin_fill()
    for _ in range(4):
        build.forward(10)
        build.left(90)
    build.end_fill()


build.color("black", "black")
build.begin_fill()

for _ in range(4):
    build.forward(450)
    build.left(90)

build.end_fill()

for _ in range(25):
    X = random.randint(-300, 150)
    Y = random.randint(-300, 150)
    build.penup()
    build.goto(X, Y)
    build.pendown()
    build.dot(1, "white")


build.goto(-300, -300)
drawOutline()


build.penup()

build.right(90)
build.forward(450)
build.right(90)
build.forward(100)
build.right(90)
build.forward(200)

build.pendown()


windows()

build.penup()
build.backward(200)
build.left(90)
build.forward(60)
build.right(90)
build.forward(80)
build.pendown()

windows()

build.penup()
build.forward(70)
build.left(90)
build.forward(170)
build.pendown()

windows()

build.penup()
build.forward(20)
build.pendown()

windows()

build.penup()
build.backward(100)
build.right(90)
build.forward(60)
build.pendown()

windows()

build.penup()
build.forward(110)
build.pendown()

windows()


build.screen.mainloop()
