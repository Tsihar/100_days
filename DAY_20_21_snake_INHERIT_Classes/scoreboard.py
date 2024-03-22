from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto((0, 280))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def count_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto((0, 0))
        self.write('Game over', align=ALIGNMENT, font=FONT)
