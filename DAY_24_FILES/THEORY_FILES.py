# 1 Базовое чтение файлов

file = open("theory_my_file.txt") # открываем файл, относительный путь потому что файл во внутр директории питона
content = file.read() # нужно сначала прочитать содержимое и в переменной будет храниться оно
print(content) # выводим содержимое файла
file.close() # обяз надо закрывать после открытия иначе он в фоне остается открытым и жрет ресурсы

# 2 продвинутое чтение файлов
with open("theory_my_file.txt") as file: # открытие файла происходит в переменную file
    content = file.read()
    print(content) # не надо закрывать файл, это автоматом происходит

# 3 написание в файлы
with open("theory_my_file.txt", mode="w") as file: # по дефолту применяется read, чтоб написать надо "w"
    file.write("I just wrote smth") # что было ранее терь удалено и записано это

# 3.1 Если файла нет, он создастся
with open("theory_new_file1.txt", mode="w") as file:
    file.write("New file")

# 3 добавление в файлы
with open("theory_my_file.txt", mode="a") as file: # "a" = append, добавляем к существующему
    file.write("\nI just wrote smth else") # в след строку

with open("data.txt") as file: # открытие файла происходит в переменную file
    content = int(file.read())
    print(type(content))
