from prettytable import PrettyTable # из пэкаджа lprettytable импортим класс PrettyTable

table = PrettyTable()  # создаем table - экземпляр класса PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"]) # передаем обязательные аргументы в метод класса

print(table.align) # вывод: {'base_align_value': 'c', 'Pokemon Name': 'c', 'Type': 'c'}
# по дефолту по центру выровнено

table.align = "l" # т к align это просто переменная,
# то как и к обычной переменной мы применяем одно из допустимых докой значений, меняя значение переменной

print(table)
