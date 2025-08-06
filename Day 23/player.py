STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.teleport(*STARTING_POSITION)
        self.setheading(90)
        
    def move_up(self):
        self.fd(MOVE_DISTANCE)

    def touch_the_line(self):
        self.teleport(*STARTING_POSITION)