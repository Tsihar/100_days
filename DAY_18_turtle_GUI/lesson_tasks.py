from turtle import *
import random
timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')
timmy.write('Score', move=False, align='center', font=('Arial', 10, 'bold'))
import turtle
# Task 1. Нарисовать квадрат
# for i in range(4):  # лучший вариант нарисовать квадрат
#     timmy.forward(100)
#     timmy.right(90)

# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)

# Task 2. Нарисовать прерывистую линию
#
# for i in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# Task 2. Нарисовать треугольник, квадрат, 5ти, 6ти, 7ми, 8ми, 9ти, 10ти угольник
# мой варик 1:
# num_of_sides = 3
# while num_of_sides <= 10:
#     degree = 360 / num_of_sides
#     for i in range(num_of_sides):
#         timmy.forward(100)
#         timmy.right(degree)
#     num_of_sides += 1
# варик с функцией 2 + цвета:
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#            "DeepSkyBlue", "LightSeaGreen", "wheat",
#            "SlateGray", "SeaGreen"]
# def draw_figures(num_of_sides):
#     degree = 360 / num_of_sides
#     for i in range(num_of_sides):
#         timmy.forward(100)
#         timmy.right(degree)
#
#
# for shape in range(3, 10):
#     timmy.color(random.choice(colours))
#     draw_figures(shape)

# Task 3. случайное блуждание
# мой вариант со ссылкой на метод, которая хранится в списке и выполняется рандомно
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#            "DeepSkyBlue", "LightSeaGreen", "wheat",
#            "SlateGray", "SeaGreen"]
# moves = [timmy.back, timmy.forward]
# turns = [timmy.right, timmy.left]
#
# for i in range(60):
#     timmy.pensize(5)
#     timmy.color(random.choice(colours))
#
#     move = random.choice(moves)
#     turn = random.choice(turns)
#     timmy.speed(8)
#     move(20)
#     turn(90)
# ее варик:
# directions = [0, 90, 180, 270]
# timmy.pensize(5)
# timmy.speed(10)
#
# for i in range(50):
#     timmy.color(random.choice(colours))
#     timmy.setheading(random.choice(directions))
#     timmy.forward(20)

# Task 4. rgb цвета
# from turtle import *
# import random
#
# timmy = turtle.Turtle()
# turtle.colormode(255)  # нужно явно указать колормод, чтобы метод pencolor применялся далее
# directions = [0, 90, 180, 270]
# timmy.pensize(5)
# timmy.speed(10)
#
# def rand_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# for i in range(50):
#     timmy.pencolor(rand_color())
#     timmy.setheading(random.choice(directions))
#     timmy.forward(20)

# Task 5. спирограф (окружности смещенные на небольшой градус и нарисованные по кругу)
# from turtle import *
# import random
#
# timmy = turtle.Turtle()
# turtle.colormode(255)
# timmy.speed(200)
#
#
# def rand_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# for i in range(72):
#     timmy.pencolor(rand_color())
#     timmy.circle(100.0)
#     timmy.left(5)
#
screen = Screen()
screen.exitonclick()
