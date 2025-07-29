number = input("Input the number of heights in cm.:")
list = number.split()
print(list)
print(len(list))
s = 0
count = 0
for i in list:
    s = s + int(i)
    count+=1
avg_height = s/count
print(avg_height)
result = round(avg_height)
print(f"The average height is {result}")