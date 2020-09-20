import turtle
turtle.speed(100)
def draw_star(angle, n):
    count = 0
    for _ in range(n):
        turtle.forward(100)
        turtle.right(angle)

n = int(input())
angle = 720 / n
draw_star(angle, n)
input()