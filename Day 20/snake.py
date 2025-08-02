from turtle import Turtle , Screen
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
    
    def create_snake(self):
        x = 0
        for i in range(3):
            self.t = Turtle()
            self.t.shape('square')
            self.t.penup()
            self.t.color('white')
            self.t.setpos(x,0)
            self.segment.append(self.t)
            x += -20


    def up(self):
        self.segment[0].setheading(90)
    
    def left(self):
        self.segment[0].setheading(180)
    
    def down(self):
        self.segment[0].setheading(270)
    
    def right(self):
        self.segment[0].setheading(0)
    
        
    def move(self):
        for i in range(len(self.segment)-1 ,0 ,-1):
            new_x = self.segment[i-1].xcor()
            new_y = self.segment[i-1].ycor()
            self.segment[i].setpos(new_x, new_y)
        self.segment[0].fd(MOVE_DISTANCE)