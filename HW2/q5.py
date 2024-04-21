import turtle

octan = turtle.Turtle()
octan.screen.bgcolor("#99d6ff")
octan.write("STOP", font=("Arial", 32, "normal"), align="center")

octan.penup()
octan.goto(-150, - 350)
octan.pendown()

for _ in range(8):
    octan.forward(300)
    octan.left(45)


octan.screen.mainloop()
