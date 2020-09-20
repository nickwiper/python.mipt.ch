import turtle
import numpy
turtle.shape('turtle')
turtle.speed(1)
def mn(j, a):
    k = ((j-2)/j)*180
    d = a * 2 * numpy.sin(numpy.pi / j)
    turtle.right(180 - k / 2)
    for i in range(j):
        turtle.forward(d)
        turtle.right(180 - k)
    turtle.left(180 - k/2)



a = 100
for j in range(3,13):
    turtle.penup()
    turtle.goto(a, 0)
    turtle
    turtle.pendown()
    mn(j, a)
    a += 50
input()