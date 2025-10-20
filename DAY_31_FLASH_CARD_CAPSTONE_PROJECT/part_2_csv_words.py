import random
from tkinter import *
import pandas


# ---------------------------- CONNECT WORDS IN CSV  ------------------------------- #

def random_word():
    data = pandas.read_csv("french_words.csv")
    data_dict = data.to_dict(orient="records")  # делает список словарей, где каждый словарь это каждая  {"назв_кол_1: знач_кол_1", "назв_кол_2: знач_кол_2"}
    return random.choice(data_dict)


def show_new_card():
    canvas.itemconfig(word_text, text=f"{random_word()['French']}")  # изменяем атрибут text переменной timer_text, чтобы на холсте менялось значение таймера
    canvas.itemconfig(lang_text, text="French")  # изменяем атрибут text переменной timer_text, чтобы на холсте менялось значение таймера


# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

# Main window
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash cards")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)  # Создание холста (Canvas)

# Images
card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
right_img = PhotoImage(file="right.png")
wrong_img = PhotoImage(file="wrong.png")

canvas.create_image(400, 262, image=card_front)  # Отображение картинки в центре холста (110, 110)
canvas.grid(column=0, row=0, columnspan=2)

# Texts
lang_text = canvas.create_text(400, 150, text='', fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text='', fill="black", font=("Ariel", 60, "bold"))

# Buttons
right_button = Button(image=right_img, highlightthickness=0, command=show_new_card)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=show_new_card)
wrong_button.grid(column=1, row=1)

show_new_card()  # Сразу показываем карточку при запуске программы

window.mainloop()
