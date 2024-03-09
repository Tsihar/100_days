import random
from turtle import Turtle, Screen

is_race_on = True
screen = Screen()
screen.setup(width=500, height=400)  # ставим размер экран
user_bet = screen.textinput(title="Сделай ставку", prompt="Введите цвет черепахи, которая выиграет гонку: ")
# выше выводим попап где юзер делает ставку
colors = ['red', 'green', 'blue', 'purple', 'yellow', 'orange']
y = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")  # при создании объекта сразу определяем его форму
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win. Winning color is {winning_color}")
            else:
                print(f"You lost. Winning color is {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
