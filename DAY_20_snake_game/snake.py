from turtle import *


class Snake:
    def __init__(self):
        self.start_positions = [
            (0, 0),
            (-20, 0),
            (-40, 0) # сделали стартовые позиции через кортеж
        ]
        self.snake = []

    def create_snake(self):
        for sn in self.start_positions:
            new_snake = Turtle(shape='square')
            new_snake.penup()
            new_snake.color('white')
            new_snake.goto(sn)  # используем каждый кортеж как координаты каждого сегмента змейки
            self.snake.append(new_snake)

    def move(self):

        for move in range(len(self.snake) - 1, 0, -1):
            new_x_cor = self.snake[move - 1].xcor()
            new_y_cor = self.snake[move - 1].ycor()
            self.snake[move].goto(x=new_x_cor, y=new_y_cor) # каждый сегмент становится на место впереди стоящего
        self.snake[0].forward(20)
