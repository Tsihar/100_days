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


guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()

    if answer_state == "Exit":
        break

    if answer_state in data.state.to_list() and answer_state not in guessed_states:
        my_states.hideturtle()
        my_states.penup()
        st_row = data[data.state == answer_state]
        my_states.goto(int(st_row.x), int(st_row.y))
        my_states.write(f'{answer_state}', font=("Courier", 8, "normal"))
        guessed_states.append(answer_state)

missed_states =
states_to_learn.csv
screen.exitonclick()





# Как получить координаты клика? 👇
# def get_mouse_click_coor(x, y):
#     print(x, y) # печатает через зпт обаа зн-ния
#
# turtle.onscreenclick(get_mouse_click_coor) #передает значения координат клика в ф-цию
#
# turtle.mainloop() # помогает держать окно открытым, даже если код кончился

