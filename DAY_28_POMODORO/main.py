from tkinter import *  # импорт всех классов модуля tkinter(Canvas, PhotoImage, Tk)
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 # плюсуется после каждого интервала (и рабочего, и короткого перерыва и длинного)
timer = None # нужна чтоб ресетать таймер


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)  # стопаем таймер
    canvas.itemconfig(timer_text, text="00:00")  # сбрасываем на 00:00
    my_label.config(text="Timer", fg=GREEN)  # называем таймер снова Timer
    my_mark.config(text="", fg=GREEN)  # удаляем галочки
    reps = 0  # повторения сбросили на 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    print(f"Completed reps: {reps}")
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        my_label.config(text="Long Break", fg=RED)
        count_down(3)
    elif reps % 2 == 0:
        my_label.config(text="Short Break", fg=PINK)
        count_down(2)
    else:
        my_label.config(text="Work", fg=GREEN)
        count_down(4)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)  # округляет в меньшую сторону
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # это динамическая типизация - сначала переменная была int, а потом стала str

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # изменяем атрибут text переменной timer_text, чтобы на холсте менялось значение таймера
    if count >= 0:
        # after выполняет указанную ф-ю через указанное время с указанным параметром
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:  # стартануть новый таймер, если счетчик меньше 0
        start_timer()
        if reps % 2 == 0: # добавляем галочку после каждого рабочего времени
            my_mark.config(text="✔"*int(reps/2), fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #
# Создание главного окна приложения с помощью Tkinter
window = Tk()

# Установка заголовка окна
window.title('Pomodoro')

# Настройка отступов по краям окна и установка фонового цвета (значение в переменной YELLOW)
window.config(padx=100, pady=30, bg=YELLOW)

#
window.after(ms=1000, )

# Лейбл
my_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), background=YELLOW)
my_label.grid(column=1, row=0)

# Создание холста (Canvas) с заданной шириной, высотой, фоновым цветом и без рамки
canvas = Canvas(width=300, height=250, bg=YELLOW, highlightthickness=0)

# Загрузка изображения из файла tomato.png
tomato_img = PhotoImage(file='tomato.png')

# Отображение изображения на холсте, центр изображения расположен в координатах (100, 120)
canvas.create_image(150, 100, image=tomato_img)

# Добавление текстового таймера на холст поверх изображения (белый цвет, шрифт задается через FONT_NAME)
timer_text = canvas.create_text(150, 120, text='00:00', fill="white", font=(FONT_NAME, 35, "bold"))

# галочка
my_mark = Label(fg=GREEN, font=(FONT_NAME, 15), bg=YELLOW)
my_mark.grid(column=1, row=3)

# calls start_timer() when pressed
button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Finish", command=reset_timer)
button_reset.grid(column=2, row=2)

# Размещение холста в главном окне
canvas.grid(column=1, row=1)

window.mainloop()
