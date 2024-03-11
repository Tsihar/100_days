import time
from turtle import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Змейка')
screen.tracer(0) # если передаем 0, то будет черный экран, пока не пропишем update для включения экрана

snake = []
start_positions = [(0, 0), (-20, 0), (-40, 0)] # сделали стартовые позиции через кортеж
for sn in start_positions:
    new_snake = Turtle(shape='square')
    new_snake.penup()
    new_snake.color('white')
    new_snake.goto(sn) # используем каждый кортеж как координаты каждого сегмента змейки
    snake.append(new_snake)

# screen.update() # включаем экран для отрисовки сразу всей змейки, а не кусками
game_is_on = True
while game_is_on: # в этом месте выполнения кода экран черный из-за tracer-a, ниже уже update отрисовывает паровоз
    screen.update()  # отрисовали весь паровоз только после движения каждого сегмента
    time.sleep(0.1)  # задерживаем, иначе код так быстро работает, что не успеваем даже увидеть змейку, так она быстро вперед убегает
    for move in snake:
        move.forward(20) # двинули каждый сегмент


screen.exitonclick()
