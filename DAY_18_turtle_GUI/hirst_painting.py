# import colorgram
#
# colors = colorgram.extract('200430102527-01-damien-hirst-severed-spots.jpg', 10)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import *
import random

color_list = [
    (53, 100, 123),
    (155, 63, 45),
    (205, 152, 24),
    (198, 13, 32),
    (248, 236, 25),
    (40, 76, 188),
    (144, 147, 53),
    (39, 216, 69),
    (238, 227, 5),
    (227, 159, 49)
]

timmy = Turtle()
turtle.colormode(255)
timmy.hideturtle()
timmy.speed("fastest")
timmy.penup()
y_pos = -200
timmy.setpos(-200, y_pos)


def draw_row():
    for i in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)

for i in range(10):
    draw_row()
    y_pos += 50
    timmy.setpos(-200, y_pos)


screen = Screen()
screen.exitonclick()
