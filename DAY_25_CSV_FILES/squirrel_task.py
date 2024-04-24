import pandas as pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = data[data["Primary Fur Color"] == "Gray"]
len_gray = len(gray)

cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
len_cinnamon = len(cinnamon)

black = data[data["Primary Fur Color"] == "Black"]
len_black = len(black)

squirrels_data= {
    "Fur color": ["grey", "cinnamon", "black"],
    "Count": [len_gray, len_cinnamon, len_black]
}

new_data = pandas.DataFrame(squirrels_data)
new_data.to_csv("squirrels_color_count.csv")

