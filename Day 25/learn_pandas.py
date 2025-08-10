import pandas

# data = pandas.read_csv("Day 25/weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

#converts to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# #converts to list
# temp_list = data["temp"].to_list()
# print(temp_list)

# # avg_temp = sum(temp_list)/ len(temp_list)
# # print(round((avg_temp),3))

# #gets the average
# print(data['temp'].mean())

# #gets maximum value
# print(data['temp'].max())

# #get data from column
# print(data.condition) # is same as print(data['condition'])

# #get the data with maximum temperature
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp.iloc[0])
# monday_temp_fah = monday_temp * (9/5) + 32
# print(monday_temp_fah)

#Create a dataframe from scratch

data_dict = {
    "students" : ['Amy', 'James', 'Angela'],
    "scores" : [46, 87, 90]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("Day 25/new_data.csv")

