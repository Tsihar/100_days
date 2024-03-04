# import turtle

# timmy = turtle.Turtle() #импортировали класс Turtle из модуля turtle
# и прикрепили его к переменной timmy

from turtle import Turtle, Screen  # из модуля turtle импортим класс Turtle

timmy = Turtle()  # создали объект timmy класса Turtle (класс всегда с большой буквы называется в отличие от переменной)
print(timmy)  # выход: "<turtle.Turtle object at 0x000001F04034D460>"
# объект Turtle сохраняется в месте памяти компьютера 0x000001F04034D460, это уже ни просто стринга или int тип данных

timmy.shape("turtle") #делает вместо курсора форму черпеахи
timmy.color("chartreuse") #в скобках передаем аргумент метода color чтоб, покрасить черепаху
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight) #выход: значение аттрибута "300"
# через точку идет обращение
# к АТРИБУТУ (то что у класса есть. как обычная переменная) класса Screen объекта my_screen

my_screen.exitonclick() #через точку идет обращение
# к МЕТОДУ (то, что класс может делать, функция класса - метод) класса Screen объекта my_screen
