from turtle import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Змейка')


# snake = []
start_positions = [(0, 0), (-20, 0), (-40, 0)]
for sn in start_positions:
    new_snake = Turtle(shape='square')
    # new_snake.shapesize(stretch_wid=1)
    new_snake.color('white')
    new_snake.goto(sn)
    # snake.append(new_snake)




screen.exitonclick()
