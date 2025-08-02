from turtle import Turtle , Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
    
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
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def left(self):
        if self.head.heading() != RIGHT:    
            self.head.setheading(LEFT)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
        
    def move(self):
        for i in range(len(self.segment)-1 ,0 ,-1):
            new_x = self.segment[i-1].xcor()
            new_y = self.segment[i-1].ycor()
            self.segment[i].setpos(new_x, new_y)
        self.segment[0].fd(MOVE_DISTANCE)