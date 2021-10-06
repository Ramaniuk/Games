import pandas
data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# average_temp = round(sum(temp_list) / len(temp_list), 2)
# max_temp = data["temp"].max()


print(data[data.temp == data.temp.max()])

