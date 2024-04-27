import time
import turtle

import pandas
data = pandas.read_csv("50_states.csv")

my_states = turtle.Turtle()
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


score = 0
while score != 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?").title()
    st_index = data.index[data.state == answer_state].to_list()[0]
    if answer_state in data.state.to_list():
        my_states.hideturtle()
        my_states.color("black")
        my_states.penup()
        my_states.goto((data[data.state == answer_state].x[st_index], data[data.state == answer_state].y[st_index]))
        my_states.write(f'{answer_state}', font=("Courier", 10, "normal"))
        score += 1






# Как получить координаты клика? 👇
# def get_mouse_click_coor(x, y):
#     print(x, y) # печатает через зпт обаа зн-ния
#
# turtle.onscreenclick(get_mouse_click_coor) #передает значения координат клика в ф-цию
#
turtle.mainloop() # помогает держать окно открытым, даже если код кончился
screen.exitonclick()
