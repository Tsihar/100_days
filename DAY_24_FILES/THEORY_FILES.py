# 1 Базовое чтение файлов

file = open("theory_my_file.txt")  # открываем файл, относительный путь потому что файл во внутр директории питона
content = file.read()  # нужно сначала прочитать содержимое и в переменной будет храниться оно
print(content)  # выводим содержимое файла
file.close()  # обяз надо закрывать после открытия иначе он в фоне остается открытым и жрет ресурсы

# 2 продвинутое чтение файлов
with open("theory_my_file.txt") as file:  # открытие файла происходит в переменную file
    content = file.read()
    print(content)  # не надо закрывать файл, это автоматом происходит

# 3 написание в файлы
with open("theory_my_file.txt", mode="w") as file:  # по дефолту применяется read, чтоб написать надо "w"
    file.write("I just wrote smth")  # что было ранее терь удалено и записано это

# # 3.1 Если файла нет, он создастся, если выбираем режимы 'a' или 'w'
# with open("theory_new_file1.txt", mode="w") as file:
#     file.write("New file")

# 3 добавление в файлы
with open("theory_my_file.txt", mode="a") as file:  # "a" = append, добавляем к существующему
    file.write("\nI just wrote smth else")  # в след строку

with open("data.txt") as file:  # открытие файла происходит в переменную file
    content = int(file.read())
    print(type(content))

# 4 Относительный путь

# 4.1 на шаг наверх
# / Root
# - Work.folder
# --report.doc # хотим обратится к этому файлу на шаг наверх
# --Project.folder # мы работаем в этой папке
# ---talk.ppt
# # нужно прописать ../report.doc , две точки обращаются на шаг наверх
#
# # 4.2 на шаг вниз
# / Root
# - Work.folder # мы работаем в этой папке
# --report.doc
# --Project.folder
# ---talk.ppt # хотим обратится к этому файлу на шаг вниз
# # нужно прописать ./Project/talk.ppt , одна точка обращаются на шаг вниз
#
# # 4.3 на том же уровне
# / Root
# - Work.folder
# --report.doc
# --Project.folder # мы работаем в этой папке
# ---talk.ppt # хотим обратится к этому файлу на шаг вниз
# # нужно прописать ./talk.ppt , одна точка обращается на тот же уровень, где и мы сидим

# 4 Абсолютный путь

# это когда прописываем полный путь с корневого диска (можно его и не указывать в пути)
# и проваливаемся внутрь папок "/Ihar/Ihar SupHelper/absolute_path.txt"
# ВСЕГДА указывать прямой слэш

# Пример абсолютного пути к файлу absolute_path.txt
with open("/Users/37529/Desktop/absolute_path.txt") as file:
    content = file.read()
    print(content)

# Пример относительного пути (относительно текущей рабочей директории)
with open("../../../Desktop/absolute_path.txt") as file:
    content = file.read()
    print(content)

# C:\Users\37529\PycharmProjects\100_days\DAY_24_FILES\ # мы тут
# C:\Users\37529\Desktop\absolute_path.txt # файл тут
#
#
# ../../../Desktop/absolute_path.txt
# первые 2 точки наверх на одну директорию - в 100_days
# след 2 точки наверх еще на одну директорию - в PycharmProjects
# след 2 точки наверх еще на одну директорию - в 37529
# и дальше уже идем вниз в папку Desktop (внутри нее наш искомый файл)
