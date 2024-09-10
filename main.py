import turtle
import time

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("pink")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def shape(x, y, size, color, thickness):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.pensize(thickness)
    t.pendown()
    t.begin_fill()
    t.left(140)
    t.forward(size)

    for _ in range(200):
        t.right(1)
        t.forward(size * 0.009)
    
    t.left(120)

    for _ in range(200):
        t.right(1)
        t.forward(size * 0.009)

    t.forward(size)
    t.end_fill()
    t.setheading(0)

shapes = [
    (0, -100, 200, "#FF9999", 4),
    (0, -90, 180, "#FFCCCC", 4),
    (0, -80, 160, "#FFE6E6", 4),
    (0, -70, 140, "#FFCCCC", 4),
    (0, -60, 120, "#FF99CC", 4),
    (0, -50, 100, "#FFCCFF", 4),
    (0, -40,  80, "#FF6666", 4),
]

for shape_args in shapes:
    shape(*shape_args)
    time.sleep(0.5)

turtle.done()