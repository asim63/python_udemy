from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x = 0 ,y = 0):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.shapesize(stretch_wid  =  5, stretch_len = 1)
        self.color('white')
        self.setpos(self.x,self.y)  

    def paddle_up(self):
        if self.ycor() < 310:
            new_y = self.ycor() + 20
            self.setpos(self.x, new_y)
        
    def paddle_down(self):
        if self.ycor() > -310:
            new_y = self.ycor() - 20
            self.setpos(self.x, new_y)