from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.move()
        
    def move(self): 
        new_x = self.xcor() + 9
        new_y = self.ycor() + 7
        self.setpos(new_x,new_y)
        