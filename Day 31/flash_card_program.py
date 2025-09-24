from tkinter import *
import random
import pandas as pd
import json 

BACKGROUND_COLOR = "#B1DDC6"
iknow_list = []
timer = None

data = pd.read_csv("Day 31\spanish-english.csv")
spanish_words = data['Spanish'].to_list()
# print(spanish_words)

#functions
def iknow(s,e):
    global iknow_list
    iknow_list.append(s)
    # print(iknow_list)
    new_data = {
        s : e
    }
    try:
        with open(r"Day 31\words_i_know.json", mode = "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
        
    data.update(new_data)
    
    with open(r"Day 31\words_i_know.json", mode = "w") as file:
        json.dump(data, file, indent = 4)
        
    show_card()

def dontknow(s,e):
    show_card()
    new_data = {
        s : e
    }
    try:
        with open(r"Day 31\words_to_learn.json", mode = "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
        
    data.update(new_data)
    
    with open(r"Day 31\words_to_learn.json", mode = "w") as file:
        json.dump(data, file, indent = 4)

def get_words():
    global iknow_list
    spanish_word = random.choice(spanish_words)
    while spanish_word in iknow_list:
        spanish_word = random.choice(spanish_words)
    english_word = data.English[data.Spanish.values == spanish_word].values[0]
    return spanish_word, english_word

def show_front(s):
    canvas1.create_image(400, 263, image=front_image)
    canvas1.create_text(400, 150, text="Spanish", font=("Ariel", 40, "italic"))
    canvas1.create_text(400, 263, text=s, font=("Ariel", 60, "bold"))

def show_back(e):
    canvas1.create_image(400, 263, image=back_image)
    canvas1.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
    canvas1.create_text(400, 263, text=e, font=("Ariel", 60, "bold"))
    
def show_card():
    global timer
    global s,e
    if timer: #to cancel old timer
        window.after_cancel(timer)  
    s,e = get_words()
    show_front(s)
    timer = window.after(3000, lambda: show_back(e)) #shows back with english text after 3 seconds

#UI setup

window = Tk()
window.config(padx = 50,pady = 50,bg = BACKGROUND_COLOR)
window.title("Flash")

front_image = PhotoImage(file = r'Day 31\images\card_front.png')
back_image = PhotoImage(file = r'Day 31\images\card_back.png')
right_image = PhotoImage(file = r'Day 31\images\right.png')
wrong_image = PhotoImage(file = r'Day 31\images\wrong.png')

canvas1 = Canvas(width = 800, height = 526, highlightthickness = 0, bg = BACKGROUND_COLOR)
canvas1.grid(row = 0, column = 0, columnspan = 2)
## To use an image as a button, you can do the following:
# my_image = PhotoImage(file="path/to/image_file.png")
# button = Button(image=my_image, highlightthickness=0)

button1 = Button(image = right_image,bg = BACKGROUND_COLOR, highlightthickness = 0,command = lambda: iknow(s,e))
button1.grid(column = 1, row = 1)

button2 = Button(image = wrong_image,bg = BACKGROUND_COLOR, highlightthickness = 0, command = lambda: dontknow(s,e))
button2.grid(column = 0, row = 1)

show_card()

window.mainloop()