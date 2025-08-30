from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
count = 4
import random

#functions
def iknow():
    global count
    count = 4

def idk():
    global count
    count = 4
    
def show_card():
    global count
    if count > 0:
        canvas1.create_image(400, 263, image = front_image)
        canvas1.create_text(400, 150, text = "French", font = ("Ariel", 40, "italic"))
        canvas1.create_text(400,263, text = "WORD", font = ("Ariel", 60 , "bold"))
    else:
        canvas1.create_image(400,263, image = back_image)
        canvas1.create_text(400, 150, text = "English", font = ("Ariel", 40, "italic"))
        canvas1.create_text(400,263, text = "WORD", font = ("Ariel", 60 , "bold"))
    print(count)
    count -= 1
    if count < 0:
        count = 0
    window.after(1000, show_card)
    
    canvas1.grid(row = 0, column = 0, columnspan = 2)
    
#UI setup

window = Tk()
window.config(padx = 50,pady = 50,bg = BACKGROUND_COLOR)
window.title("Flash")

front_image = PhotoImage(file = r'Day 31\images\card_front.png')
back_image = PhotoImage(file = r'Day 31\images\card_back.png')
right_image = PhotoImage(file = r'Day 31\images\right.png')
wrong_image = PhotoImage(file = r'Day 31\images\wrong.png')

canvas1 = Canvas(width = 800, height = 526, highlightthickness = 0, bg = BACKGROUND_COLOR)
show_card()

# my_image = PhotoImage(file="path/to/image_file.png")
# button = Button(image=my_image, highlightthickness=0)
button1 = Button(image = right_image,bg = BACKGROUND_COLOR, highlightthickness = 0,command = iknow)
button1.grid(column = 1, row = 1)

button2 = Button(image = wrong_image,bg = BACKGROUND_COLOR, highlightthickness = 0, command = idk)
button2.grid(column = 0, row = 1)

window.mainloop()