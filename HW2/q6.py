# import turtle

# tri = turtle.Turtle()
# tri.screen.bgcolor("#99d6ff")
# tri.hideturtle()


# def triangle(x, y, color):

#     tri.penup()
#     tri.goto(x, 0)
#     tri.pendown()

#     tri.color(color)

#     tri.begin_fill()
#     for _ in range(3):
#         tri.forward(y)
#         tri.left(120)
#     tri.end_fill()


# x = tri.screen.numinput(
#     "X", "Please enter the X coordinate: ", 10, minval=- 500, maxval=500)
# y = tri.screen.numinput(
#     "Y", "Please enter the Y coordiante: ", 10, minval=10, maxval=500)
# color = tri.screen.textinput("color", "Please enter the desirable color: ")

# triangle(x, y, color)


# tri.screen.mainloop()


import turtle

tri = turtle.Turtle()
tri.screen.bgcolor("#99d6ff")

def Triangle(x1, x2, x3, y1, y2, y3, color):
    tri.penup()
    tri.goto(x1, y1)
    tri.pendown()
    
    tri.color(color, color)
    
    tri.begin_fill()
    tri.goto(x2, y2)
    tri.goto(x3, y3)
    tri.goto(x1, y1)
    tri.end_fill()

x1 = tri.screen.numinput("X1 input", "Please enter the X1 coordinate: ", default = 0, minval = -300, maxval = 300)
y1 = tri.screen.numinput("Y1 input", "Please enter the Y1 coordinate: ", default = 0, minval = -300, maxval = 300)
x2 = tri.screen.numinput("X2 input", "Please enter the X2 coordinate: ", default = 100, minval = -300, maxval = 300)
y2 = tri.screen.numinput("Y2 input", "Please enter the Y2 coordinate: ", default = 100, minval = -300, maxval = 300)
x3 = tri.screen.numinput("X3 input", "Please enter the X3 coordinate: ", default = -200, minval = -300, maxval = 300)
y3 = tri.screen.numinput("Y3 input", "Please enter the Y3 coordinate: ", default = 200, minval = -300, maxval = 300)

color = tri.screen.textinput("choose color", "Please enter the desire color: ")

Triangle(x1, x2, x3, y1, y2, y3, color)

tri.screen.mainloop()