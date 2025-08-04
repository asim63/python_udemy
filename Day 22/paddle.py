from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x = 0 ,y = 0):
        super().__init__()
        self.x = x
        self.y = y
        self.segment = []
        self.hideturtle()
        self.color('white')
        self.create_paddle()
        
    def create_paddle(self):
        for i in range(3):
            self.make_paddle(self.x,self.y)
            self.y -=20
        
    def make_paddle(self,x,y):
        self.t = Turtle()
        self.t.shape('square')
        self.t.penup()
        self.t.color('white')
        self.t.setpos(x,y)
        self.segment.append(self.t)
        
    