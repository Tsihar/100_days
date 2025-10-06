from tkinter import *

# Класс Tk
window = Tk() #
window.title("My first GUI program") # тайтл окна программы
window.minsize(width=500, height=300) # мин размер окна
window.config(padx=50, pady=50) # добавляет padding всему окну - отступ слева/справа и снизу/сверху

# Класс Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold")) # Если будет только эта строка, то ничего не выведется в окне
# my_label.pack()
# my_label.pack(side="left") # этот метод добавляет на экран текст выше и автоматом центрирует
# аргумент side отправляет текст в нужное место в зав-ти от значений
# bottom, left, right, top
# аргумент expand=True сетит текст в середину окна

# засетить новый текст (установленный при определении объекта класса) можно 2мя способами:
my_label['text'] = 'New text'  # 1 обращением к параметру text как мы обращаемся к ключу в словаре меняя его зн-ние
my_label.config(text="New text") # 2 через метод config
# my_label.place(x=0, y=0) # ставит элемент в нудное место по координатам, но не оч эффективно
my_label.grid(column=0, row=0) # визуально делит окно на табличку и ставит в указанную колонку и в ряд
# grid должен использоваться вместо метода pack
my_label.config(padx=50, pady=50) # добавляет паддинг для виджета
#!!! Компонент Создания кнопки

def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")
    my_label.config(text=input.get())

button1 = Button(text='Click me', command=button_clicked)
# через параметр command передается ф-ция, которая будет отрабатывать при клеке по кнопке

# !!!Задание: вывести на экране текст "Button got clicked" вместо текущего текста "New text"
# в метод button clicked добавляем метод на изменение текст лейбла
button1.grid(column=1, row=1)
# button.pack()

# !!!Задание: добавить новую кнопку по визуальной таблице грид в 3ю колонку и 1й ряд
button2 = Button(text='New button')
button2.grid(column=2, row=0)

#!!! Компонент создания поля ввода
def get_input():
    my_label.config(text=input.get())


input = Entry(width=10)  # width сетит ширину поля
input.grid(column=3, row=2)
# input.pack()


# !!! Задание: то, что написали в поле ввода вывести в лейбл
# в метод button clicked добавляем метод на изменение текст лейбла,
# добавляя в значение text метод input.get(), который получает текст из поля ввода

# import turtle
#
# tom = turtle.Turtle()
# tom.write("Some text", align="left") # при наведении курсора много всяких аргументов у класса Turtle
# # те, кот имеют знак "=..." означает, что заданы по дефолту значения уже
# # arg нужно указывать - это текст и он обязателен при вызове метода write
# # если я хочу изменить какое-то дефолтное, я просто указываю его через зпт, наприм align="left"

#Каждый класс (label, button, entry и т д) называется виджет
window.mainloop() # сохраняет открытым окно и должно быть всегда последним, кот примерно является циклом while True и поэтому постоянно открыто