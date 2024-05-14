# Так выглядит код с ограниченным кол-вом аргументов ф-ции
def add1(n1, n2):
    return n1 + n2


add1(n1=5, n2=3)


# Что, если надо неограниченное их кол-во - это Unlimited Positional Arguments

def add2(*args): # звездочка значит любое кол-во аргументов, которое передадим при вызове ф-ции
    # вместо args можно давать любое имя наприм *numbers, args - принято дефолтным
    print(args[0]) # т к args - кортеж, можно обратится к любому его значению через индекс
    r = 0
    for i in args:
        r += i
    return r

print(add2(7, 3, 4, 2)) # эти аргументы дают кортеж, кот можно спокойно лУпить
# Вывод: 16

def test(*args):
    print(args) # на выходе тип "кортеж" - (1, 2, 3, 5)


test(1, 2, 3, 5)

# Что, если надо неограниченное кол-во keyword аргументов - это Unlimited Keyword Arguments

def calculate(**kwargs): # 2 звездочки значит любое кол-во keyword аргументов
    print(kwargs) # это тип данных словарь dict {'add': 3, 'multiply': 5}
    for key, value in kwargs.items():
        print(key) # Вывод "add 3" на разных строках
        print(value) # Вывод "multiply 5" на разных строках
        print(kwargs["add"]) # Вывод 3

calculate(add=3, multiply=5)

# Задание: что выведет след ф-ция
def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64) # Вывод: 4 (7, 3, 0) {"x":10, "y":64}
# 4 передается по позиции. 7,3,0 собираются в кортеж. x и y находятся в словаре
def calculate1(n, **kwargs): # n = 2
    n += kwargs["add"] # сначала 2+3 = 5
    n *= kwargs["multiply"] # потом 5*5=25
    print(n) # Вывод 25

calculate1(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"] # make - ключ
        self.model = kw["model"] # model - ключ

# my_car = Car() # при наведении мышкой мы видим только **kw, аргументов make и модель питон не предлагает,
# потому что это опциональные keyword аргументы
# my_car = Car(make="Nissan", model="GT-R") # Nissan и GT-R - значения соотв-щих ключей
# print(my_car.model) # Вывод GT-R
# my_car = Car(make="Nissan")
# print(my_car.model) # Вывод: ошибка KeyError: 'model', т к при определении объекта не задал model
# чтобы не получить ошибку KeyError можно использовать метод get при инициализации класса
class Car1:

    def __init__(self, **kw):
        self.make = kw.get("make") # make - ключ
        self.model = kw.get("model") # model - ключ

my_car1 = Car1(make="Nissan")
print(my_car1.model) # Вывод: None
# потому что мы не засетили его