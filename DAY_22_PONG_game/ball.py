from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        next_pos_x = self.xcor() + self.x_move #* ind_x
        next_pos_y = self.ycor() + self.y_move #* ind_y
        self.goto(next_pos_x, next_pos_y)

    def bounce_side_walls(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9 # выбрали умножение, чтобы не могла стать минусом скорость иначе будет ошибка

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1 # возвращаем скорость в исходное значение, когда мяч ресетится
        self.paddle_bounce()

