# Library to extract colors from an image. I don´t need that in the code,
# but i´ll leave here as a reference to be used in the future in "How to extract colors from an image".

# import colorgram
#
# colors = colorgram.extract('dots.jpg', 20)
# colors_list = []
#
# for i in range(20):
#     first_color = colors[i]
#     rgb = tuple(first_color.rgb)
#     colors_list.append(rgb)

import turtle as t
import random


colors_list = [(236, 35, 108), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40),
               (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93),
               (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]


# Function to make the dot walk 10 paces and then stop
def straight():
    for _ in range(10):
        tim.penup()
        tim.dot(20, random.choice(colors_list))
        tim.forward(50)


# Function to find the dot position and arranje to the next level, until reach 10
def level_positions():
    position = -162.13
    for _ in range(10):
        straight()
        tim.goto(-212.13, position)
        position += 50


# Function to start from the set position, as shown in the Grapich Interface.
def initial_position():
    tim.penup()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)


# Turtle definitions as speed, name, color and hide.
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
tim.hideturtle()


# Starting the program
if __name__ == '__main__':
    initial_position()
    level_positions()


# That makes the Grapigh Interface appear and stay, until we click to exit.
screen = t.Screen()
screen.exitonclick()
