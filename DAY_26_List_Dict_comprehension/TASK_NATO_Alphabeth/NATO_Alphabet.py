import pandas
name = input("Enter the name: ").upper()

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(data_dict)

code_list = [data_dict[i] for i in name]
print(code_list)