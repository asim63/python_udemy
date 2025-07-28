from turtle import Turtle, Screen
import random 
t = Turtle()
def change_colour():
    R = random.random()
    B = random.random()
    G = random.random()
    
    t.color(R,G,B)
    
for item in range(3,11):
    
    n = 360/item
    change_colour()
    for _ in range (item):
        
        t.fd(100)
        t.right(n)
    
    
screen = Screen()
screen.exitonclick()