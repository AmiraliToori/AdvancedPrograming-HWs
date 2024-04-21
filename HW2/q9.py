
import turtle

check = turtle.Turtle()
check.speed(10)
check.screen.bgcolor("#99d6ff")
check.hideturtle()

check.penup()
check.goto(-350, -200)
check.pendown()

check.color("black")


def black():
    check.begin_fill()
    for _ in range(4):
        check.forward(100)
        check.left(90)
    check.end_fill()
    check.forward(100)


def white():
    for _ in range(4):
        check.forward(100)
        check.left(90)
    check.forward(100)


def upper_floor():
    check.left(180)
    check.forward(500)
    check.right(90)
    check.forward(100)
    check.right(90)


for _ in range(4):
    check.forward(500)
    check.left(90)

count = 0
while (True):

    black()
    count += 1
    if (count % 5 == 0):
        upper_floor()

    if (count == 25):
        break

    white()
    count += 1
    if (count % 5 == 0):
        upper_floor()


check.screen.mainloop()
