import turtle as t
import random

t.colormode(255)


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


gui = t.Turtle()
gui.speed('fastest')

for _ in range(90):
    gui.color(color())
    gui.circle(100)
    gui.left(4)


screen = t.Screen()
screen.exitonclick()
