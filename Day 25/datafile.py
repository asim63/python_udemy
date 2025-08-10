# with open(r"Day 25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
    
# import csv
# with open(r"Day 25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []

#     # skips header    
#     next(data)
    
#     for row in data:
#         temperature = int(row[1])
#         temp.append(temperature)


import pandas

data = pandas.read_csv("Day 25/weather_data.csv")
print(data["temp"])