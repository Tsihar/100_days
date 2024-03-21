# есть родительский класс
class Animal:
    def __init__(self):
        self.name_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):  # в скобках родительский класс
    def __init__(self):
        super().__init__()  # эта строчка позволяет наследовать все атрибуты и методы у родительского класса

    def breathe_extra(self):
        super().breathe() # используем все из метода супер класса
        print('breathe under water') # и добавляем немного нового

    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.swim()  # Moving in water
nemo.breathe() # Inhale, exhale, nemo может и дышать т к унаследовал метод breathe класса Animal
print(nemo.name_eyes) # 2, атрибут тоже унаследован nemo
nemo.breathe_extra() # Inhale, exhale breathe under water (каждый print на отдельной строке)