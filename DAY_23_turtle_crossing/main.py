import time
from turtle import Screen

from DAY_23_turtle_crossing.scoreboard import Scoreboard
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Не собьешь!")
screen.tracer(0)

cars = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.cars_move()

    # столкновение с машиной
    for car in cars.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


    # увеличение счетчика на 1, ресет позиции и увеличение скорости
    if player.ycor() >= 290:
        player.reset_position()
        scoreboard.level_up()
        cars.new_speed_level()

screen.exitonclick()