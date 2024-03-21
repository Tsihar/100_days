import random
from turtle import Turtle


class Food(Turtle): # наследуем класс Turtle
    def __init__(self):
        super().__init__() # наследуем атрибуты и методы класса Turtle
        # благодаря наследованию, можем использовать методы класса Turtle, как например ниже
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # делаем круг 10*10
        self.color('blue')
        self.speed('fastest')
        self.refresh() # мы создали метод, а не унаследовали

    def refresh(self): # еда в новую локацию перемещается
        rand_x = random.randint(-200, 280) # выбираем в пределах экрана 300*300
        rand_y = random.randint(-200, 280)
        self.goto(rand_x, rand_y)