from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

import random

# my_image = PhotoImage(file="path/to/image_file.png")
# button = Button(image=my_image, highlightthickness=0)

#UI setup
window = Tk()
window.config(padx = 50,pady = 50,bg = BACKGROUND_COLOR)
window.title("Flash")
canvas = Canvas()
canvas.create_image("Day 31/image/card_front.png")
canvas.pack()

window.mainloop()