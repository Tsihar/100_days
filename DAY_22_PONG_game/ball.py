from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('white')
        self.penup()

    def move(self, ind_x, ind_y):
        next_pos_x = self.xcor() + 10 * ind_x
        next_pos_y = self.ycor() + 10 * ind_y
        self.goto(next_pos_x, next_pos_y)

    def bounce(self):

