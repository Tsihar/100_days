import random
import time
from turtle import Turtle
# from random import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.create_car()
        self.start_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle('square')
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        # car.goto(-40, 0)
        car.goto(310, random.randint(-260, 260))
        self.cars.append(car)

    def cars_move(self):
        if random.randint(2, 12) == 5:
            self.create_car()
        for car in self.cars:
                car.back(self.start_speed)


    # def car_generator(self):
    #     # self.create_car()
    #     if random.randint(2, 12) == 5:
    #         self.create_car()

    def new_speed_level(self):
        self.start_speed += MOVE_INCREMENT


