import time
from turtle import *

from DAY_24_FILES.food import Food
from DAY_24_FILES.scoreboard import Scoreboard
from DAY_24_FILES.snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Змейка')
screen.tracer(0) # если передаем 0, то будет черный экран, пока не пропишем update для обновления экрана, для отрисовки
screen.listen()

snake = Snake()
food = Food() # еда уже нарисуется сразу на экране после запуска
scoreboard = Scoreboard()

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

    # определить столкновение змейки с едой
    if snake.head.distance(food) < 15: # можно поиграться с этим числом чтоб красиво было столкновение
        # print('nom nom')
        scoreboard.count_score() # увеличиваем счет когда съедаем еду
        food.refresh()
        snake.extend_snake()

    # определить столкновение змейки со стеной
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    # определить столкновение со своим хвостом
    for i in snake.snake[1:]:
        if snake.head.distance(i) <= 10:
            scoreboard.reset()
            snake.reset()







screen.exitonclick()
