from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, start_pos_x, start_pos_y):
        super().__init__()
        # self.pos_x = start_pos_x  # в этом походу нет необходимости
        # self.pos_y = start_pos_y  # в этом походу нет необходимости
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto((start_pos_x, start_pos_y))
        # self.paddles = []
        # self.create_paddle(self.pos_x, self.pos_y) # сначала я сделал без супер класса
        # print(self.paddles[0])

    # def create_paddle(self, start_pos_x, start_pos_y):
    #     paddle = Turtle('square') # но с супер классом, необходимо было создавать объект, чтоб далее описать paddle
    #     paddle.color('white')
    #     paddle.shapesize(stretch_wid=5, stretch_len=1)
    #     paddle.penup()
    #     paddle.goto((start_pos_x, start_pos_y))
    #     paddle.paddles.append(paddle)
    def move_up(self):
        new_ycor = self.ycor() + MOVE_DISTANCE  # ссылка идет сразу на объект класса из файла main
        self.goto((self.xcor(), new_ycor))

    def move_down(self):
        new_ycor = self.ycor() - MOVE_DISTANCE  # такая же тема, что и чуть выше
        self.goto((self.xcor(), new_ycor))
