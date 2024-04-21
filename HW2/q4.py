import turtle

hyp = turtle.Turtle()
hyp.speed(10)
hyp.screen.bgcolor("#99d6ff")


i = 10
for _ in range(100):
    hyp.left(90)
    hyp.forward(i)
    i += 7

hyp.screen.mainloop()
