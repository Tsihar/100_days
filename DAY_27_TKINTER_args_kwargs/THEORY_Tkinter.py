import tkinter

# Класс Tk
window = tkinter.Tk() #
window.title("My first GUI program") # тайтл окна программы
window.minsize(width=500, height=300) # мин размер окна

# Класс Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold")) # Если будет только эта строка, то ничего не выведется в окне
my_label.pack(side="left") # этот метод добавляет на экран текст выше и автоматом центрирует
# аргумент side отправляет текст в нужное место в зав-ти от значений
# bottom, left, right, top
# аргумент expand=True сетит текст в середину окна

import turtle

tom = turtle.Turtle()
tom.write("Some text", align="left") # при наведении курсора много всяких аргументов у класса Turtle
# те, кот имеют знак "=..." означает, что заданы по дефолту значения уже
# arg нужно указывать - это текст и он обязателен при вызове метода write
# если я хочу изменить какое-то дефолтное, я просто указываю его через зпт, наприм align="left"

window.mainloop() # сохраняет открытым окно и должно быть всегда последним, кот примерно является циклом while True и поэтому постоянно открыто