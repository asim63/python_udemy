import random
names = input("Input the names of peoples.")

list = names.split(", ")
print(list)
print(len(list))
num = random.randint(0,(len(list)-1))
print(num)
print(f"{list[num]} will pay for the dinner today.!")