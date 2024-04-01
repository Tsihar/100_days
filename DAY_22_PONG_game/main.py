import time
from turtle import Turtle
from turtle import Screen
from DAY_22_PONG_game.paddles import Paddle
from DAY_22_PONG_game.ball import Ball
from DAY_22_PONG_game.scoreboard import Scoreboard

speed = 0.08

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


scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # отскок от стены
    if ball.ycor() >= 281 or ball.ycor() <= -281:
        ball.bounce_side_walls()

    # отскок от ракетки
    if ball.distance(paddle_right) < 50 and ball.xcor() > 330 or ball.distance(paddle_left) < 50 and ball.xcor() < -330:
        # больше 330 нужно для того, чтобы мяч, если приблизится на 40, но не коснется ракетки,
        # приблизился ближе по х, тогда будет видимость касания
        ball.paddle_bounce()
        while ball.distance(paddle_right) < 50: # если это не сделать, то шарик троит около ракетки
            ball.move()
            screen.update()
            time.sleep(ball.ball_speed)

    # если правая рокетка промахнулась
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.count_score_left()

    # если левая рокетка промахнулась
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.count_score_right()

screen.exitonclick()
