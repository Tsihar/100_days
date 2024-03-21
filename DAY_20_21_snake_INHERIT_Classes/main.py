import time
from turtle import *

from DAY_20_21_snake_INHERIT_Classes.snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Змейка')
screen.tracer(0) # если передаем 0, то будет черный экран, пока не пропишем update для включения экрана
screen.listen()

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# screen.update() # включаем экран для отрисовки сразу всей змейки, а не кусками
game_is_on = True

while game_is_on: # в этом месте выполнения кода экран черный из-за tracer-a, ниже уже update отрисовывает паровоз
    screen.update()  # отрисовали весь паровоз только после движения каждого сегмента
    time.sleep(0.1)  # задерживаем, иначе код так быстро работает, что не успеваем даже увидеть змейку, так она быстро вперед убегает



    snake.move()





screen.exitonclick()