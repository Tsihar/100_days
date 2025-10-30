import random
from tkinter import *
import pandas


# ---------------------------- CONNECT WORDS IN CSV  ------------------------------- #
ALL_WORDS_CSV = "french_words.csv"
NEW_WORDS_CSV = "new_words.csv"

try:
    data = pandas.read_csv(NEW_WORDS_CSV)
except FileNotFoundError:
    origin_data = pandas.read_csv(ALL_WORDS_CSV)
    data_dict = origin_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")  # делает список словарей, где каждый словарь это каждая  {"назв_кол_1: знач_кол_1", "назв_кол_2: знач_кол_2"}
    ran_word = {}


def show_french_card():
    global flip_timer, ran_word
    window.after_cancel(flip_timer)  # при клике в любое время таймер сбрасывается и появляется новое слово и стартует новый таймер, т к эти переменные глобальные
    ran_word = random.choice(data_dict)

    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(word_text, text=f"{ran_word['French']}", fill="black")  # изменяем атрибут text переменной timer_text, чтобы на холсте менялось значение таймера
    canvas.itemconfig(lang_text, text="French", fill="black")  # изменяем атрибут text переменной timer_text, чтобы на холсте менялось значение таймера
    flip_timer = window.after(3000, show_english_card, ran_word['English'])


def remove_word_from_list():
    data_dict.remove(ran_word)
    print(len(data_dict))
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("new_words.csv", index=False)
    show_french_card()  # после удаления слова из списка показываем новое слово из невыученного списка


def show_english_card(english_word):
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{english_word}", fill="white")

# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

# Main window
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash cards")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)  # Создание холста (Canvas)


flip_timer = window.after(3000, show_english_card)

# Images
card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
right_img = PhotoImage(file="right.png")
wrong_img = PhotoImage(file="wrong.png")

card_image = canvas.create_image(400, 262, image=card_front)  # Отображение картинки в центре холста (110, 110)
canvas.grid(column=0, row=0, columnspan=2)

# Texts
lang_text = canvas.create_text(400, 150, text='', fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text='', fill="black", font=("Ariel", 60, "bold"))

# Buttons
right_button = Button(image=right_img, highlightthickness=0, command=remove_word_from_list)  # После нажатия надо удалить слово
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=show_french_card)
wrong_button.grid(column=1, row=1)

show_french_card()  # Сразу показываем карточку при запуске программы

window.mainloop()
