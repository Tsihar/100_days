# 1. Откроем файл csv содержащий данные о погоде
# with open("weather_data.csv") as data:
#     data_weather = data.readlines()
#     print(data_weather)
# Чтоб получить чистый список в коде выше из
# необходимых значений нужно много кода, чтоб убрать лишнее

# 2. Откроем файл csv пом csv библиотеки
# import csv
#
# with open("weather_data.csv") as data:
#     data = csv.reader(data) # <_csv.reader object at 0x000001C93069B9A0>
#     print(data) # data - это итеративный объект со строками
#
#     temperature = []
#     for row in data:
#         print(row)
# вывод:
# ['day', 'temp', 'condition']
# ['Monday', '12', 'Sunny'] # и т д построчно

# 3. Задание: вывести в списке только температуры
# import csv
#
# with open("weather_data.csv") as data:
#     data = csv.reader(data)
#
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# видно, что, чтобы вывести список температуры нужно много строк кода
# и чтобы избежать этого используюем package PANDAS

# 4. PANDAS - либа для работы с разными таблицами
import pandas

data = pandas.read_csv("weather_data.csv") # Достаточно указать путь к файлу, но есть и много других
# опциональных аргументов у метода read_csv
print(data)
# Вывод:
#          day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain

print(data["temp"]) # указывает только имя колонки и получаем все температуры одной строкой
