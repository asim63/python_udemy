with open(r"Day 25/weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
    
import csv
with open(r"Day 25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    print(data)
    # for row in data:
    #     temperature = int(row[1])
    #     print(temperature)
        
    next(data)
    for row in data:
        temperature = int(row[1])
        print(temperature)
        
    # print(data)
    # # temp = []
    # for row in data:
        
    #     temperature = int(row[1])
    #     print(temperature)
        