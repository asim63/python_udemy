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
        self.mid = self.segment[1]
        self.head = self.segment[0]
        self.tail = self.segment[2]
        
    def create_paddle(self):
        for i in range(4):
            self.make_paddle(self.x,self.y)
            self.y -=20
        
    def make_paddle(self,x,y):
        self.t = Turtle()
        self.t.shape('square')
        self.t.setheading(90)
        self.t.penup()
        self.t.color('white')
        self.t.setpos(x,y)
        self.segment.append(self.t)
        
    def paddle_up(self):
        if self.mid.ycor() < 310:
            self.mid.fd(20)
        
    def paddle_down(self):
        if self.mid.ycor() > -310:
            self.mid.bk(20)
        
    def paddle_move(self):
            new_y = self.mid.ycor()
            self.head.setpos(self.x,new_y + 20)
            self.tail.setpos(self.x,new_y - 20)