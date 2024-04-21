import turtle

star = turtle.Turtle()
star.hideturtle()
star.screen.bgcolor("#99d6ff")

for _ in range(8):
    star.left(45)
    star.forward(200)
    star.left(180)

star.screen.mainloop()
