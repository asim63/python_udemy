FONT = ("Courier", 16, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.setpos(-280,260)
        self.hideturtle()
        self.update()
        
    def update(self):
        self.write(f"Level:{self.level}", font = FONT)
        
    def increment(self):
        self.clear()
        self.level += 1
        self.update()