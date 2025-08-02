from turtle import Turtle , Screen
class Snake:

    def __init__(self):
        self.segment = []
        x = 0
        for i in range(3):
            t = Turtle()
            t.shape('square')
            t.penup()
            t.color('white')
            t.setpos(x,0)
            self.segment.append(t)
            x += -20

    def move(self):
        for i in range(len(self.segment)-1 ,0 ,-1):
            new_x = self.segment[i-1].xcor()
            new_y = self.segment[i-1].ycor()
            self.segment[i].setpos(new_x, new_y)
        self.segment[0].fd(20)