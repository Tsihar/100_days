import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
MAIN_FILE_NAME = "data.json"


# Password Generator Project
def gen_passw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]  # choice и randint импортирован из random напрямую
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    pass_list = pass_letters + pass_symbols + pass_numbers
    shuffle(pass_list)  # импортирован из random напрямую

    password = "".join(pass_list)

    # вставляем пароль в поле и копируем в буфер обмена через предустановленный пэкадж pyperclip
    psw_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def read_data(file_name):
    with open(file_name, mode="r") as file:
        data = json.load(fp=file)
        return data


def write_data(file_name, data_to_write):
    with open(file_name, mode="w") as file:
        json.dump(obj=data_to_write, fp=file, indent=4)
        print(data_to_write)
        return data_to_write


def save_pass():
    website = website_input.get()
    email = email_input.get()
    password = psw_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if not all([email, password]):
        messagebox.showwarning(title="Warning!", message="Please don't leave any fields empty")
    else:
        try:
            data = read_data(MAIN_FILE_NAME)

        except FileNotFoundError:
            write_data(MAIN_FILE_NAME, new_data)

        else:
            data.update(new_data)
            write_data(MAIN_FILE_NAME, data)

        finally:  # если файл не нашли и записали данные или добавили данные надо все равно почистить поля
            website_input.delete(0, END)
            psw_input.delete(0, END)
            website_input.focus()


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_psw():
    try:
        data = read_data(MAIN_FILE_NAME)
    except FileNotFoundError:
        messagebox.showwarning(title="No saved passwords", message="Please, create your first password")
    else:
        site_search = website_input.get()
        search_result = data.get(site_search, None)
        if search_result:
            messagebox.showinfo(title="Here is your data",
                                message=f"Email: {search_result['email']}\n"
                                        f"Password: {search_result['password']}")
        else:

            messagebox.showwarning(title="Please try again", message="No data about the resource")

        website_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()  # Создание главного окна приложения с помощью Tkinter
canvas = Canvas(width=300, height=220)  # Создание холста (Canvas)
logo_img = PhotoImage(file="logo.png")

window.title('Pass manager')
window.config(padx=50, pady=70)  # Настройка отступов по краям окна
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
website_input = Entry(width=23)
website_input.grid(column=1, row=1, sticky="w")
website_input.focus()  # курсор активен в поле при старте

email_input = Entry(width=42)
email_input.grid(column=1, row=2, columnspan=2, sticky="w")
email_input.insert(0, "ihar@email.com")  # поле предзаполнено с начала строки

psw_input = Entry(width=23)
psw_input.grid(column=1, row=3, columnspan=2, sticky="w")

# Buttons
generate_button = Button(text='Generate password', command=gen_passw)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=35, command=save_pass)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

search_button = Button(text='Search', command=search_psw)
search_button.grid(column=2, row=1)

canvas.grid()  # Размещение холста в главном окне
window.mainloop()  # сохраняет открытым окно
