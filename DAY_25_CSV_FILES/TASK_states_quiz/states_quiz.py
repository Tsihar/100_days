import time
import turtle

import pandas

# поднимаем экран с фоном-гифкой
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# повторяем пока не наберем 50 штатов в списке guessed states
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()

# если вводим Exit, то создаем файл с неотгаданными штатами
    if answer_state == "Exit":
        states = [state for state in all_states if state not in guessed_states] # формируем список неотгаданных штатов
        # for state in all_states: # код без list comprehension
        #     if state in guessed_states:
        #         all_states.remove(state)
        missed_states = pandas.DataFrame(states)
        missed_states.to_csv("states_to_learn.csv")
        break
# если ответ совпадает со штатом из данных csv, то пишем на карте в штате по его координатам его название
    if answer_state in all_states and answer_state not in guessed_states: # + проверка, что ответа нет в списке угаданных, чтоб не дублировались
        my_states = turtle.Turtle()
        my_states.hideturtle()
        my_states.penup()
        st_row = data[data.state == answer_state]
        my_states.goto(int(st_row.x), int(st_row.y)) # координаты штата из файла
        my_states.write(f'{answer_state}', font=("Courier", 8, "normal")) # написали на карте штат в положенном месте
        guessed_states.append(answer_state) # добавляем штат в список отгаданных штатов



screen.exitonclick()





# Как получить координаты клика? 👇
# def get_mouse_click_coor(x, y):
#     print(x, y) # печатает через зпт обаа зн-ния
#
# turtle.onscreenclick(get_mouse_click_coor) #передает значения координат клика в ф-цию
#
# turtle.mainloop() # помогает держать окно открытым, даже если код кончился

