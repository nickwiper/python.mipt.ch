import turtle
turtle.speed(100)
turtle.shape('turtle')
j = 1
for i in range(10):
    turtle.circle(i * 10 * j)
    j *= -1
    turtle.circle(i * 10 * j)
input()