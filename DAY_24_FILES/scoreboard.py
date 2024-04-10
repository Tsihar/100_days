from turtle import Turtle

ALIGNMENT = 'left'
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score = 0
        self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto((-100, 280))
        self.write(f'Score: {self.score}  High score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def count_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto((-50, 0))
    #     self.write('Game over', align=ALIGNMENT, font=FONT)
