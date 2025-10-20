from tkinter import *


# ---------------------------- UI SETUP ------------------------------- #
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
canvas.create_text(400, 150, text='Lang', fill="black", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text='Word', fill="black", font=("Ariel", 60, "bold"))

# Buttons
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=1, row=1)

window.mainloop()
