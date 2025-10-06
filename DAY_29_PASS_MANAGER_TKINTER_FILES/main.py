from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pass():
    with open("data.txt", mode="a") as file:
        file.write(f"{website_input.get()} | {email_input.get()} | {psw_input.get()}\n")
        website_input.delete(0, END)
        email_input.delete(0, END)
        psw_input.delete(0, END)
        website_input.focus()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()  # Создание главного окна приложения с помощью Tkinter
canvas = Canvas(width=300, height=220)  # Создание холста (Canvas)
logo_img = PhotoImage(file="logo.png")

window.title('Pass manager')
window.config(padx=50, pady=50)  # Настройка отступов по краям окна
canvas.create_image(100, 100, image=logo_img)  # Отображение картинки в центре холста (110, 110)
canvas.grid(column=1, row=0, columnspan=2)

# Labels
website_text = Label(text="Website:", font=("Calibri", 10))
website_text.grid(column=0, row=1)

email_text = Label(text="Email/Username:", font=("Calibri", 10))
email_text.grid(column=0, row=2)

psw_text = Label(text="Password:", font=("Calibri", 10))
psw_text.grid(column=0, row=3)

# Entries
website_input = Entry(width=42)
website_input.grid(column=1, row=1, columnspan=2, sticky="w")
website_input.focus()  # курсор активен в поле при старте

email_input = Entry(width=42)
email_input.grid(column=1, row=2, columnspan=2, sticky="w")
email_input.insert(0, "ihar@email.com")  # поле предзаполнено с начала строки

psw_input = Entry(width=23)
psw_input.grid(column=1, row=3, columnspan=2, sticky="w")

# Buttons
generate_button = Button(text='Generate password')
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=35, command=save_pass)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

canvas.grid()  # Размещение холста в главном окне
window.mainloop()  # сохраняет открытым окно
