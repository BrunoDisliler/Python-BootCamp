from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def backwards():
    tim.back(10)


def turn_right():
    tim.right(10)


def turn_letf():
    tim.left(10)


def clear():
    tim.reset()


screen.listen()
screen.onkeypress(key='w', fun=forward)
screen.onkeypress(key='s', fun=backwards)
screen.onkeypress(key='a', fun=turn_letf)
screen.onkeypress(key='d', fun=turn_right)
screen.onkeypress(key='c', fun=clear)
screen.exitonclick()
