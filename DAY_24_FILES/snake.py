from turtle import Turtle
# from turtle import Screen
# screen = Screen()

START_POSITIONS = [
    (0, 0), (-20, 0), (-40, 0)  # сделали стартовые позиции через кортеж
]
MOVE_DISTANCE = 20
# создаем константы для того, чтобы менять если что их в одном месте, а не везде по коду искать
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake() # при создании объекта в конструкторе создается и сегмент змейки
        self.head = self.snake[0] # вынесли голову отдельно, т к она поворачивает всю змейку
    def create_snake(self):
        for position in START_POSITIONS:
            self.create_segment(position)

    def create_segment(self, position):
        new_snake = Turtle(shape='square')
        new_snake.penup()
        new_snake.color('white')
        new_snake.goto(position)  # используем каждый кортеж как координаты каждого сегмента змейки
        self.snake.append(new_snake)

    def reset(self):
        for seg in self.snake:
            seg.hideturtle() # убрать с экрана змейку
        self.snake.clear() # тут и далее создаем новую змею
        self.create_snake()
        self.head = self.snake[0]

    def extend_snake(self):
        self.create_segment(self.snake[-1].position())

    def move(self):
        for move in range(len(self.snake) - 1, 0, -1):
            new_x_cor = self.snake[move - 1].xcor()
            new_y_cor = self.snake[move - 1].ycor()
            self.snake[move].goto(x=new_x_cor, y=new_y_cor)  # каждый сегмент становится на место впереди стоящего
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT: # нельзя в противоположную сторону идти
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT: # нельзя в противоположную сторону идти
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN: # нельзя в противоположную сторону идти
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP: # нельзя в противоположную сторону идти
            self.head.setheading(DOWN)