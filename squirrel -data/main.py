# data from
# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = data["Primary Fur Color"].unique()
colors_dictionary = {}
for color in colors:
    colors_dictionary[color] = 0

for color in data["Primary Fur Color"]:
    colors_dictionary[color] += 1

data_frame = pandas.DataFrame.from_dict(colors_dictionary, orient='index')
data_frame.to_csv("main_colors of_central_park_squirrel.csv")


print(data_frame)