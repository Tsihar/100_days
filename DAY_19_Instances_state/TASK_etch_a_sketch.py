from turtle import Turtle, Screen

tim = Turtle()


def forwards():
    tim.forward(20)


def backwards():
    tim.back(20)


def counter_clockwise():
    tim.left(15)


def clockwise():
    tim.right(15)


def clear_screen():
    tim.reset()

screen = Screen()

screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
