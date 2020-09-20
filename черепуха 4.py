import turtle
turtle.shape('turtle')
a = 10
for j in range(10):
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)
    turtle.left(135)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.right(135)
    a += 2*10*(1 / 2 ** 0.5)
input()
