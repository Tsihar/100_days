import pandas as pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_data = data["Primary Fur Color"]
# print(color_data)

gray_squirrels = 0
for gray in color_data:
    if gray == "Gray":
        gray_squirrels += 1

print(gray_squirrels)

