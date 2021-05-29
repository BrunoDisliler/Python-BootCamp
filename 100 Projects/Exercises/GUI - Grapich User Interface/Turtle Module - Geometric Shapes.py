# Grapich User Interface used to show a geometric draw

import turtle as t
import random

tin = t.Turtle()

colours = ["dark slate gray", "sandy brown", "dark red", "indian red",
           "medium violet red", "blue violet", "blue", "dim gray"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tin.forward(100)
        tin.right(angle)


for shape_side_n in range(3, 11):
    tin.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = t.Screen()
screen.exitonclick()
