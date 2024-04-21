import turtle

sq = turtle.Turtle()

sq.hideturtle()
sq.screen.bgcolor("#99d6ff")
sq.speed(1000)
i = 10

sq.penup()
sq.goto(470, -400)
sq.pendown()


sq.right(180)
for _ in range(100):
    for _ in range(4):
        sq.forward(i)
        sq.right(90)
    i += 5

sq.screen.mainloop()
