with open("file1.txt") as file1:
    content_file1 = file1.readlines()
    list1 = [int(i) for i in content_file1] # создаем список интовый
    print(list1)
with open("file2.txt") as file2:
    content_file2 = file2.readlines()
    list2 = [int(i) for i in content_file2]
    print(list2)
list = [int(i) for i in list1 if i in list2]
print(list)

with open("file1.txt") as file1:
    list_1 = file1.readlines() # записываем каждую строку в эл-нт списка
    print(list_1)
with open("file2.txt") as file2:
    list_2 = file2.readlines()
    print(list_2)
result = [num for num in list_1 if num in list_2] # int как то избавляется от "\n"

# Your code above 👆
print(result)