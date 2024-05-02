#!!! 1 Базовая Схема

#!!! newlist = [expression for item in iterable]

# имеем код как обычно пишем:

numbers = [1, 2, 3]
new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)


new_list = [n+1 for n in numbers] # список numbers взяли сверху
# берем в квадратные скобки все выражение, в котором сохранится новый список после выполнения кода
# n+1 - это то, что делаем в рамках цикла с переменной n на каждой итерации, а именно
# к каждому элементу списка прибавляем 1

# Работа со стрингой
name = "Angela"
new_letters = [letter for letter in name] # letter на каждой итерации добавляется в список
print(new_letters) # Вывод: ['A', 'n', 'g', 'e', 'l', 'a']

# Задание взять range от 1 до 5(не включая) и каждое значение умножить на два и добавить в список
new_range = [n*2 for n in range(1, 5)]
print(new_range) # Вывод: [2, 4, 6, 8]

#!!! 2 С условием

# newlist = [expression for item in iterable if condition]
# expression выполнится только когда условие будет true

# Пример:
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# Необходимо получить имена в которых имя меньше 4х букв
short_names = [name for name in names if len(name) <= 4] # тфьу на каждой итерации добавляется в список
print(short_names) # Вывод: ['Alex', 'Beth', 'Dave']

# Задание: сделать все имена с больше, чем 5 букв, в списке и капсом
caps_names = [name.upper() for name in names if len(name) >= 5] # name.upper() - имя, попадающее под условие,
# записывается в список caps_names капсом
print(caps_names)

# Задание: есть стринга, создать список из стринг, превратить каждый эл-нт списка в число,
# и добавить только четное число в новый список
stri = "1, 1, 2, 3, 5, 8, 13, 21, 34, 55"
list_of_strings = stri.split(',') # разбили по запятой, создав список стринг
list_of_integers = [int(num) for num in list_of_strings] # добавили в список каждую разбитую стрингу как число
result = [i for i in list_of_integers if i % 2 == 0] # добавили только четное число в новый список
print(result)
