from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

import random
#functions
def iknow():
    pass
def idk():
    pass


#UI setup
window = Tk()
window.config(padx = 50,pady = 50,bg = BACKGROUND_COLOR)
window.title("Flash")
canvas1 = Canvas(width = 800, height = 526, highlightthickness = 0, bg = BACKGROUND_COLOR)
front_image = PhotoImage(file = r'Day 31\images\card_front.png')
back_image = PhotoImage(file = r'Day 31\images\card_back.png')
right_image = PhotoImage(file = r'Day 31\images\right.png')
wrong_image = PhotoImage(file = r'Day 31\images\wrong.png')
canvas1.create_image(400, 263, image = front_image)
canvas1.grid(row = 0, column = 0, columnspan = 2)

canvas1.create_text(400, 150, text = "French", font = ("Ariel", 40, "italic"))
canvas1.create_text(400,263, text = "WORD", font = ("Ariel", 60 , "bold"))

# my_image = PhotoImage(file="path/to/image_file.png")
# button = Button(image=my_image, highlightthickness=0)
button1 = Button(image = right_image,bg = BACKGROUND_COLOR, highlightthickness = 0,command = iknow)
button1.grid(column = 1, row = 1)

button2 = Button(image = wrong_image,bg = BACKGROUND_COLOR, highlightthickness = 0, command = idk)
button2.grid(column = 0, row = 1)

window.mainloop()