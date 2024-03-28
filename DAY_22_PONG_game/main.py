import time
from turtle import Turtle
from turtle import Screen
from DAY_22_PONG_game.paddles import Paddle
from DAY_22_PONG_game.ball import Ball


screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)


paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)
screen.listen()

ball = Ball()

screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

game_is_on = True
index_x = 1
index_y = 1
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move(index_x, index_y)

    # столкновение со стеной
    if ball.ycor() >= 281 or ball.ycor() <= -281:
        index_y -= 2


screen.exitonclick()