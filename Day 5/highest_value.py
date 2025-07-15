scores = input("Input the Scores: ")
list = scores.split()
count = 0
for i in list:
    count += 1
for i in range(0, len(list)):
    list[i] = int(list[i])
print(list)
print(f"Count is {count}")
highest_marks = 0

for i in range(0,count):
    if(list[i] > highest_marks):
        highest_marks = list[i]

print(f"The highest marks is {highest_marks}")
print(type(highest_marks))
