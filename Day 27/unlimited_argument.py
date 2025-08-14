# def add(*arg):
#     total = 0
#     # print(arg) #its a tuple
#     for n in arg:
#         total += n
#     return total

# print(add(5,4,3,2,1))



# def calculate(n,**kwargs):
#     print(kwargs)
#     # for(key,value) in kwargs.items():
#     n += kwargs['add']
#     n *= kwargs['multiply']
#     return n
    
# print(calculate(2, add = 3, multiply = 5))

class Car:
    
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        
my_car = Car(make ="Nissan", color = 'Blue')
print(my_car.model)
print(my_car.color)