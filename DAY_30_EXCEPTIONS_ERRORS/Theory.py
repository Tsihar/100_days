# try: # То, что может вызвать исключение
# except: # Делай это, если возникло исключение
# else: # Делай это, если не было исключений
# finally: # Делай это при любых раскладах

# FileNotFound
try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["kadabra"])
except FileNotFoundError:
    # выполняется только если файла выше нет
    # если не указывать тип ошибки оставив "except:", то мы пропускаем ошибку KeyError в print()
    # поэтому нельзя оставлять эксепшн голым
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_msg:
    # Ловим KeyError (вылезет только если файл найдётся)
    # Записываем текст ошибки в переменную error_msg и делаем красивый вывод
    print(f"The key {error_msg} doesn't exist")
    # вывод: The key 'kadabra' doesn't exist
else:
    # Выполнится только если блок try пройдет успешно,
    # иначе закончится на ошибках FileNotFoundError или KeyError
    content = file.read()
    print(content)
finally:
    # Выполняется всегда, будь то ошибка или успешное прохождение блока try
    file.close()  # файл открыт не в with поэтому надо закрывать иначе утекает память
    print("File was closed")

# FileNotFound
# with open("file.txt") as file:
#     file.read()

# KeyError
# dictionary = {"key": "value"}
# value = dictionary["non_existing_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

