# Grapich User Interface Used to demonstrate a random walk with random rgb colors.

import turtle as t
import random

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


tom = t.Turtle()
tom.shape('classic')
tom.width(15)
tom.speed('fastest')
directions = [0, 90, 180, 270]


for _ in range(200):
    tom.color(random_color())
    tom.forward(30)
    tom.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
