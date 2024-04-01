from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto((0, 250))
        self.score_left = 0
        self.score_right = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'{self.score_left}  :  {self.score_right}', align=ALIGNMENT, font=FONT)

    def count_score_left(self):
        self.score_left += 1
        self.update_scoreboard()

    def count_score_right(self):
        self.score_right += 1
        self.update_scoreboard()