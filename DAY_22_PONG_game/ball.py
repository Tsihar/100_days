from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        next_pos_x = self.xcor() + self.x_move #* ind_x
        next_pos_y = self.ycor() + self.y_move #* ind_y
        self.goto(next_pos_x, next_pos_y)

    def bounce(self):
        self.y_move *= -1

