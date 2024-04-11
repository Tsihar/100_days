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
        with open("data.txt") as best_score: # берем из файла текущий рекорд
            self.high_score = int(best_score.read())
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
            with open("data.txt", mode="w") as best_score: # записываем в файл рекорд, чтоб при запуске заново мы сразу видели текущий рекорд
                best_score.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto((-50, 0))
    #     self.write('Game over', align=ALIGNMENT, font=FONT)
