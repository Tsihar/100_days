from turtle import Turtle

START_POSITIONS = [
    (0, 0), (-20, 0), (-40, 0)  # сделали стартовые позиции через кортеж
]
MOVE_DISTANCE = 20
# создаем константы для того, чтобы менять если что их в одном месте, а не везде по коду искать


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake() # при создании объекта в конструкторе создается и сегмент змейки

    def create_snake(self):
        for sn in START_POSITIONS:
            new_snake = Turtle(shape='square')
            new_snake.penup()
            new_snake.color('white')
            new_snake.goto(sn)  # используем каждый кортеж как координаты каждого сегмента змейки
            self.snake.append(new_snake)

    def move(self):
        for move in range(len(self.snake) - 1, 0, -1):
            new_x_cor = self.snake[move - 1].xcor()
            new_y_cor = self.snake[move - 1].ycor()
            self.snake[move].goto(x=new_x_cor, y=new_y_cor)  # каждый сегмент становится на место впереди стоящего
        self.snake[0].forward(MOVE_DISTANCE)
