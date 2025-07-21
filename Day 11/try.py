import random
a = [1,2,3,4,5]

# for i in range(0,100):
#     b = random.randint(0,10)
#     print(b)
s = 0
for i in range(0,len(a)):
    s += a[i]
print(s)