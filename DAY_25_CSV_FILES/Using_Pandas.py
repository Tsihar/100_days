import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data)) # тип данных: <class 'pandas.core.frame.DataFrame'>
print(type(data["temp"])) # тип данных: <class 'pandas.core.series.Series'>

# !!! 2 ключевых структуры данных в PANDAS - Series и DataFrame:
# DataFrame - эквивалент таблицы на одной странице документа
# Series - что-то типо списка, например колонка в таблице - это Series

data_dict = data.to_dict() # сконвертить всю таблицу в словарь
print(data_dict)
# Вывод: {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

data_list = data["temp"].to_list() # сконвертить колонку в список
print(data_list)
# Вывод: [12, 14, 15, 14, 21, 22, 24]

# Задание 1: найти среднюю температуру из таблицы
# Классич вариант:
avg_temp1 = sum(data_list) / len(data_list)
print(round(avg_temp1, 2))
# Вывод: 17.43

# Pandas вариант:
avg_temp2 = data["temp"].mean() #!!! Важно: пандас чувствителен к регистру,
# поэтому при обращении к колонке важно учитывать регистр названия колонки
print(avg_temp2)
# Вывод: 17.428571428571427

# Задание 2: найти макс температуру из таблицы
max_temp = data["temp"].max()
print(max_temp)
# Вывод: 24

# !!! Как еще обратится к колонке?
print(data.condition) # PANDAS может обращаться к колонке как к обычному атрибуту
# одинаково, если написать data["temp"] или написать data.temp
# Вывод:
# 0     Sunny
# 1      Rain
# 2      Rain


# !!! Как получить все данные из строки, а не из колонки?
print(data[data.day == "Monday"]) # Выбираем колонку day и фильтруем по условию Monday, что возвращает строку, содержащую день Monday
# Вывод: 0  Monday    12     Sunny

# Задание 3: получить строку c максимальной температурой
print(data[data.temp == data.temp.max()]) # Выбираем колонку temp и фильтруем по условию макс зн-ния температуры,
# что возвращает строку, содержащую эту макс темпу
# Вывод: 6  Sunday    24     Sunny

# !!! Что если мы хотим получить только одно опред значение из строки
monday = data[data.day == "Monday"] # сохранили строку Monday в переменной
print(monday.condition) # находим Sunny через название колонки, кот оно нах-ся
# Вывод: 0    Sunny

# Задание 3: получить температуру в понедельник и сконвертить ее в Фаренгейты
monday = data[data.day == "Monday"] # получили одну строку
monday_temp = monday.temp[0] # !!! значение по каждой колонке - это список,
# !!! в колонке temp одно значение - 12, и оно первое,
# !!! соотв-но обращаемся к нему как к первому элементу списка temp[0]

monday_temp_fahr = monday_temp * 9/5 + 32
print(monday_temp_fahr)
# Вывод: 53.6

# !!! Как создать DataFrame(всю таблицу) c нуля?
# есть словарь:
data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 66, 65]
}
new_data = pandas.DataFrame(data_dict) # c пом метода DataFrame и передачи в него словаря, образуем табличку
print(new_data)
# Вывод:
#   students  scores
# 0      Any      76
# 1    James      66
# 2   Angela      65

# Табличку можно сразу конвертить в csv
new_data.to_csv("new_data.csv") # созданную табличку закидываем в csv