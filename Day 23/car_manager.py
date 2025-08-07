COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
import random
from turtle import Turtle


class CarManager():
    
    def __init__(self):
        self.move = 5
        self.cars = []
        
    def create_a_car(self):
        
        if random.randint(1,4) == 1 :
            t = Turtle('square')
            t.penup()
            t.shapesize(stretch_wid  =  1, stretch_len = 2)
            random_y = random.randint(-250,280)
            t.teleport(300,random_y)
            t.color(random.choice(COLORS))
            self.cars.append(t) 

    def move_cars(self):
        for car in self.cars:
            car.bk(self.move)
            
        
    def level_increase(self):
        self.move += 5