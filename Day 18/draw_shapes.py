from turtle import Turtle, Screen
import random 
t = Turtle()
t.speed(0)
def change_colour():
    R = random.random()
    B = random.random()
    G = random.random()
    
    t.color(R,G,B)
    
for item in range(25,50):
    
    n = 360/item
    change_colour()
    for _ in range (item):
        
        t.fd(20)
        t.right(n)
        
    new_x = t.xcor()
    y = t.ycor()
    t.setpos(new_x ,y + 2)
    
    
screen = Screen()
screen.exitonclick()