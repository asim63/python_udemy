from turtle import Turtle
import random
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.list = [-10,10]
        self.x_move = random.choice(self.list)
        self.y_move = random.randint(-10,10)
        self.move()

    def reball(self):
        self.goto(0,0)
        self.color('white')
        self.x_move = random.choice(self.list)
        self.y_move = random.randint(-10,10)
        self.move()
      
    def move(self): 
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x,new_y)
    
    def bounce(self):
        self.y_move *= -1
        
    def bounce_with_paddle(self):
        self.x_move *= -1
        
        
    #detect collision