import turtle
turtle.speed(100)
def o(j):
    for i in range(180):
        turtle.forward(2)
        turtle.right(1)
    for i in range(180, 360):
        turtle.forward(0.1)
        turtle.right(1)

turtle.shape('turtle')
turtle.left(90)
for i in range(6):
    o(i)
input()