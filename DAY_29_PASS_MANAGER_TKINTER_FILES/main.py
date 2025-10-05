from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()  # Создание главного окна приложения с помощью Tkinter
canvas = Canvas(width=220, height=220)  # Создание холста (Canvas)
logo_img = PhotoImage(file="logo.png")

window.title('Pass manager')
window.config(padx=20, pady=20)  # Настройка отступов по краям окна
canvas.create_image(100, 100, image=logo_img)  # Отображение картинки в центре холста (110, 110)


canvas.grid()  # Размещение холста в главном окне
window.mainloop()  # сохраняет открытым окно
