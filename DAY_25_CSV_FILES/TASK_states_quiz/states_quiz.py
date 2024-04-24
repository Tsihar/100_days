import turtle

import pandas
data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)




answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?").title()
print(data.state)
st = data[data.state == answer_state]
print(st)
# score = 0
# while score != 50:
if answer_state in data.state:
    turtle.hideturtle()
    turtle.color("black")
    turtle.goto(data[data.state == answer_state].x.index, data[data.state == answer_state].y.index)
    turtle.write(f'{answer_state}', font=("Courier", 20, "normal"))





# Как получить координаты клика? 👇
# def get_mouse_click_coor(x, y):
#     print(x, y) # печатает через зпт обаа зн-ния
#
# turtle.onscreenclick(get_mouse_click_coor) #передает значения координат клика в ф-цию
#
# turtle.mainloop() # помогает держать окно открытым, даже если код кончился
screen.exitonclick()
