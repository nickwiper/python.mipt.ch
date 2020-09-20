import turtle
turtle.shape('turtle')
turtle.speed(100000000)
a = 0.1
for i in range(360 * 6):
    turtle.forward(a)
    turtle.right(1)
    a *= 1.001
input()