from turtle import Turtle , Screen

t = Turtle()

def move_forward():
    t.fd(10)
    
def move_backward():
    t.bk(10)

def counter_clockwise():
    t.left(20)

def clockwise():
    t.right(20)
    
def erase():
    t.reset()
    
    

screen = Screen()
screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(erase, "c")
screen.exitonclick()