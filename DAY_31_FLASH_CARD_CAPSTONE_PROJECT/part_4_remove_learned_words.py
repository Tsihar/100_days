import random
from tkinter import *
import pandas


# ---------------------------- CONNECT WORDS IN CSV  ------------------------------- #

def random_word():
    try:
        data = pandas.read_csv("new_words_list.csv")
        data_dict = data.to_dict(orient="records")  # делает список словарей, где каждый словарь это каждая  {"назв_кол_1: знач_кол_1", "назв_кол_2: знач_кол_2"}
        return random.choice(data_dict)
    except FileNotFoundError:
        data = pandas.read_csv("french_words.csv")
        data_dict = data.to_dict(orient="records")  # делает список словарей, где каждый словарь это каждая  {"назв_кол_1: знач_кол_1", "назв_кол_2: знач_кол_2"}
        return random.choice(data_dict)

# ----------------------------- SHOW WORD CARDS ------------------------------------ #

def show_french_card():
    global flip_timer, ran_word
    window.after_cancel(flip_timer)  # при клике в любое время таймер сбрасывается и появляется новое слово и стартует новый таймер, т к эти переменные глобальные
    ran_word = random_word()
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(word_text, text=f"{ran_word['French']}", fill="black")  # изменяем атрибут text переменной timer_text, чтобы на холсте менялось значение таймера
    canvas.itemconfig(lang_text, text="French", fill="black")  # изменяем атрибут text переменной timer_text, чтобы на холсте менялось значение таймера
    flip_timer = window.after(3000, show_english_card, ran_word['English'])




def show_english_card(english_word):
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{english_word}", fill="white")

# ----------------------------- REMOVE LEARNED WORDS ------------------------------------ #
def remove_word():
    try:
        all_words = pandas.read_csv("new_words_list.csv")
    except FileNotFoundError:
        pandas.read_csv("french_words.csv")
    else:
        all_words_dict = all_words.to_dict(orient="records")
        all_words_dict.remove(ran_word)
    new_words = pandas.DataFrame(all_words_dict)
    new_words.to_csv("new_words_list.csv", index=False)

# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

# Main window
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash cards")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)  # Создание холста (Canvas)
ran_word = random_word()
flip_timer = window.after(3000, show_english_card, ran_word['English'])

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
right_button = Button(image=right_img, highlightthickness=0, command=show_french_card)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=show_french_card)
wrong_button.grid(column=1, row=1)

show_french_card()  # Сразу показываем карточку при запуске программы

window.mainloop()
