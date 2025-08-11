import pandas as pd
data = pd.read_csv("Day 25/squirrel_data.csv")
print(data["Primary Fur Color"])

grey_squirrels_count = len(data[data["Primary Fur Color"]== "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"]== "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"]== "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels_count,cinnamon_squirrels_count, black_squirrels_count]
} 

df = pd.DataFrame(data_dict)
df.to_csv("Day 25/Squirrel_count.csv")