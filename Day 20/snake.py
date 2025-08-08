from turtle import Turtle , Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        
    def create_snake(self):
        for i in range(3):
            self.add_segment(self.x,self.y)
            self.x += -20
            self.y = 0

    def add_segment(self, x, y):
        segment = Turtle('square')
        segment.penup()
        segment.color('white')
        segment.setpos(x, y)
        self.segment.append(segment)

    
    def extend(self):
        new_x = self.segment[-1].xcor()
        new_y = self.segment[-1].ycor()
        self.add_segment(new_x,new_y)

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
    
    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.x = 0
        self.y = 0
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]
        
    def move(self):
        for i in range(len(self.segment)-1 ,0 ,-1):
            new_x = self.segment[i-1].xcor()
            new_y = self.segment[i-1].ycor()
            self.segment[i].setpos(new_x, new_y)
        self.segment[0].fd(MOVE_DISTANCE)