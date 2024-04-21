# 8. Turtle Graphics: Rectangular Pattern
# In a program, write a function named drawPattern that uses the turtle graphics library
# to draw the rectangular pattern shown in Figure 5-31. The drawPattern function should
# accept two arguments: one that specifies the pattern’s width, and another that specifies the
# pattern’s height. (The example shown in Figure 5-31 shows how the pattern would appear
# when the width and the height are the same.) When the program runs, the program should
# ask the user for the width and height of the pattern, then pass these values as arguments to
# the drawPattern function



import turtle
import math

rectan = turtle.Turtle()
rectan.hideturtle()
rectan.pensize(2)
rectan.speed(100)
rectan.screen.bgcolor("#99d6ff")

rectan.penup()
rectan.goto(-200, -200)
rectan.pendown()

def makeBigger(h, w, diagonal):
    diagonal += (diagonal / 2)
    h *= 1.5
    w *= 1.5
    return h, w, diagonal

def drawShape(h, w):
    for _ in range(2):
        rectan.forward(h)
        rectan.left(90)
        rectan.forward(w)
        rectan.left(90)



def drawPattern(h, w):
    diagonal = math.sqrt(h ** 2 + w ** 2)
    if w == h:
        degree = 45
    else:
        radian = math.acos(h / diagonal)
        degree = math.degrees(radian)
    
    rectan.color("black", "black")
    
    rectan.begin_fill()
    drawShape(h, w)
    rectan.end_fill()
    
    
    rectan.right(180 - degree)
    rectan.forward(diagonal / 4)
    rectan.left(180 - degree)
    
    h, w, diagonal = makeBigger(h,  w, diagonal)
    
    drawShape(h, w)
    
    rectan.right(180 - degree)
    rectan.forward(diagonal / 4)
    rectan.left(180 - degree)
    
    h, w, diagonal = makeBigger(h,  w, diagonal)
    
    drawShape(h, w)
    
    rectan.left(degree)
    rectan.forward(diagonal)
    
    rectan.right(180 - (90 - degree))
    rectan.forward(w)
    rectan.right(180 - (90 - degree))
    rectan.forward(diagonal)
    
    rectan.left(180 - (90 - degree))
    rectan.forward(w / 2)
    rectan.left(90)
    rectan.forward(h / 2)
    
    for _ in range(2):
        rectan.forward(h / 2)
        rectan.backward(h / 2)
        rectan.right(90)
        rectan.forward(w / 2)
        rectan.backward(w / 2)
        rectan.right(90)
    

height = rectan.screen.numinput("height","Please enter the height.", default = 100, minval = 20, maxval = 600)
width = rectan.screen.numinput("width","Please enter the width.", default = 100, minval = 20, maxval = 600)


drawPattern(height, width)

rectan.screen.mainloop()











#####################################################################################################################

# import turtle
# import math

# rectan = turtle.Turtle()
# rectan.hideturtle()
# rectan.pensize(2)
# rectan.screen.bgcolor("#99d6ff")


# def drawPattern(h, w):
#     diagonal = math.sqrt(h ** 2 + w ** 2)
#     if w == h:
#         degree = 45
#     else:
#         radian = math.acos(h / diagonal)
#         degree = math.degrees(radian)

#     rectan.color("black", "black")

#     rectan.begin_fill()
#     for _ in range(2):
#         rectan.forward(h)
#         rectan.left(90)
#         rectan.forward(w)
#         rectan.left(90)
#     rectan.end_fill()

#     rectan.right(180 - degree)
#     rectan.forward(diagonal / 2)
#     rectan.left(180 - degree)

#     new_diagonal = 0
#     new_diagonal += diagonal

#     for _ in range(2):
#         rectan.forward(h * 2)
#         rectan.left(90)
#         rectan.forward(w * 2)
#         rectan.left(90)

#     rectan.right(180 - degree)
#     rectan.forward(diagonal / 2)
#     rectan.left(180 - degree)

#     new_diagonal += diagonal

#     for _ in range(2):
#         rectan.forward(h * 3)
#         rectan.left(90)
#         rectan.forward(w * 3)
#         rectan.left(90)

#     h *= 3
#     w *= 3

#     rectan.left(degree)
#     rectan.forward(new_diagonal * (3 / 2))
#     rectan.right(180 - degree)
#     rectan.forward(w)
#     rectan.right(180 - degree)
#     rectan.forward(new_diagonal * (3 / 2))

#     rectan.left(180 - degree)
#     rectan.forward(w / 2)
#     rectan.left(90)

#     rectan.forward(w)
#     rectan.left(90)
#     rectan.forward(w / 2)
#     rectan.left(90)
#     rectan.forward(w / 2)
#     rectan.left(90)
#     rectan.forward(w)


# height = rectan.screen.numinput(
#     "height", "Please enter the height.", default=100, minval=20, maxval=600)
# width = rectan.screen.numinput(
#     "width", "Please enter the width.", default=100, minval=20, maxval=600)


# drawPattern(height, width)

# rectan.screen.mainloop()


#################################################################################################################


# import turtle
# import math

# rectan = turtle.Turtle()

# rectan.screen.bgcolor("#99d6ff")
# rectan.penup()
# rectan.goto(-250, - 250)
# rectan.pendown()
# rectan.speed(10)
# rectan.hideturtle()

# DIAGONAL = math.sqrt(250**2 + 250**2)
# OUTER_DIAGONAL = math.sqrt(DIAGONAL**2 + DIAGONAL**2)

# for _ in range(4):
#         rectan.forward(500)
#         rectan.left(90)

# for _ in range(6):
#     rectan.forward(250)
#     rectan.left(90)

# for _ in range(8):
#     rectan.left(45)
#     rectan.forward(DIAGONAL)
#     rectan.left(180)
#     rectan.forward(DIAGONAL)

# for _ in range(2):
#     rectan.right(90)
#     rectan.forward(DIAGONAL)

# rectan.right(90)

# for _ in range(4):
#     rectan.forward(DIAGONAL * 2)
#     rectan.right(90)

# rectan.right(45)
# rectan.forward(OUTER_DIAGONAL)

# for _ in range(4):
#     for _ in range(2):
#         rectan.forward(OUTER_DIAGONAL)
#         rectan.left(180)
#     rectan.left(90)

# rectan.left(90)

# rectan.forward((3/4) * DIAGONAL)
# rectan.right(135)
# rectan.fillcolor("black")
# rectan.begin_fill()
# for _ in range(4):
#     rectan.forward(375)
#     rectan.right(90)
# rectan.end_fill()


# rectan.screen.mainloop()
