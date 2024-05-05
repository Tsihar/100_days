student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

# Looping through dict
# for (key, value) in student_dict.items():
#     print(key, value)

# Вывод:
# student ['Angela', 'James', 'Lilly']
# score [56, 76, 98]

import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

for (key, value) in student_data_frame.items():
    print(value) # Выводит все значения по каждой колонке
    print(key) # Выводит название каждой колонке

# Вывод value:
# 0    Angela
# 1     James
# 2     Lilly
# Name: student, dtype: object
# 0    56
# 1    76
# 2    98
# Name: score, dtype: int64

# Вывод key:
# student
# score

# !!! так лупить через цикл неудобно, поэтому у пандас для этого свой метод
# Лупить по строкам
for (index, row) in student_data_frame.iterrows():
    # print(index) # выведет имеющиеся индексы
    # print(row) # выведет имеющиеся строки по одной
    # print(row.student) # выведет имеющиеся имена студентов в каждой строке
    if row.student == "Angela":
        print(row.score) # Выведет оценку Angela = 56
# Вывод row:
# student    Angela
# score          56
# Name: 0, dtype: object
# student    James
# score         76
# Name: 1, dtype: object
# student    Lilly
# score         98
# Name: 2, dtype: object