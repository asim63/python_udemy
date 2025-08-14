# def add(*arg):
#     total = 0
#     # print(arg) #its a tuple
#     for n in arg:
#         total += n
#     return total

# print(add(5,4,3,2,1))



def calculate(n,**kwargs):
    print(kwargs)
    print(n)
    # for(key,value) in kwargs.items():
    n += kwargs['add']
    print(n)
    n *= kwargs['multiply']
    return n
    
print(calculate(2, add = 3, multiply = 5))