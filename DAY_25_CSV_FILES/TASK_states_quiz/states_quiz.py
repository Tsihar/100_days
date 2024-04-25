import time
import turtle

import pandas
data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)




answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?").title()
print(data.state)
st = data[data.state == answer_state]
st_index = data.index[data.state == answer_state].to_list()[0]
print(st_index)
print(st)
coord = data[data.state == answer_state].x[st_index]
print(coord)
# score = 0
# while score != 50:
if answer_state in data.state:
    turtle.hideturtle()
    turtle.color("black")
    turtle.penup()
    turtle.goto((data[data.state == answer_state].x[st_index], data[data.state == answer_state].y[st_index]))
    turtle.write(f'{answer_state}', font=("Courier", 10, "normal"))
    time.sleep(1)
    screen.update()






# Как получить координаты клика? 👇
# def get_mouse_click_coor(x, y):
#     print(x, y) # печатает через зпт обаа зн-ния
#
# turtle.onscreenclick(get_mouse_click_coor) #передает значения координат клика в ф-цию
#
# turtle.mainloop() # помогает держать окно открытым, даже если код кончился
screen.exitonclick()
