import turtle
turtle.speed(100)
def o(j):
    turtle.right(360 / 6)
    for i in range(360):
        turtle.forward(2)
        turtle.right(1)

turtle.shape('turtle')
for i in range(6):
    o(i)
input()